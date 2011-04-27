#!/usr/bin/env python

# Copyright 2006, 2008 Jonathan Jacky
# 
# This file works with GNU Radio, available from http://gnuradio.org/trac
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from gnuradio import gr, gru
from gnuradio.eng_option import eng_option
from optparse import OptionParser
from gnuradio.wxgui import stdgui2, fftsink2, scopesink2, form
#from gnuradio_local.wxgui import multigui
import multigui # import local version possibly with multi mods
import wx
import sys

# constants determined externally
usrp_full_scale = 32767

# control panel text
signal_string = { gr.GR_SIN_WAVE : "Sine" }
noise_string = { gr.GR_UNIFORM : "Uniform, amplitude is peak-to-peak",
                 gr.GR_GAUSSIAN : "Gaussian, amplitude is variance" }

# defaults, can be overridden by command line 
default_rate = 1e5
default_signal_type = gr.GR_SIN_WAVE
default_freq = 8000
default_ampl = usrp_full_scale
default_noise_type = gr.GR_GAUSSIAN
default_noise_ampl = 1000 # just enough to make it interesting
default_frame_decim = 3
default_v_scale = 10000
default_t_scale = 50e-6
default_ref_level = 100

class app_flow_graph(stdgui2.std_top_block):
    def __init__(self, frame, panel, vbox, argv, panel_info):
        stdgui2.std_top_block.__init__(self, frame, panel, vbox, argv)

        signal_type = default_signal_type # not yet an option

        # command line options
        parser = OptionParser(option_class=eng_option)
        parser.add_option("-r", "--sample-rate",type="eng_float",
                          default=default_rate,
                          help="set flow graph sample rate [default=%s]" % default_rate)
        parser.add_option ("-f", "--freq", type="eng_float",
                           default=default_freq,
                           help="set signal frequency [default=%s]" % default_freq)
        parser.add_option ("-a", "--amplitude", type="eng_float",
                           default=default_ampl,
                           help="set signal amplitude [default %s]" % default_ampl)
        parser.add_option ("--gaussian", dest="noise_type",
                           action="store_const", const=gr.GR_GAUSSIAN,
                           help="generate Gaussian noise (-x is variance)",
                           default=default_noise_type)
        parser.add_option ("--uniform", dest="noise_type",
                           action="store_const", const=gr.GR_UNIFORM,
                           help="generate Uniform noise (-x is peak-to-peak)")
        parser.add_option ("-x", "--noise_amplitude", type="eng_float",
                           default=default_noise_ampl,
                           help="set noise amplitude (variance or p-p) [default %s]" % default_noise_ampl)
        parser.add_option("-n", "--frame_decim", type="int",
                          default=default_frame_decim,
                          help="set oscope frame decimation factor to DECIM [default=%s]" % default_frame_decim)
        parser.add_option("-v", "--v_scale", type="eng_float",
                          default=default_v_scale,
                          help="set oscope initial V/div [default=%s]" % default_v_scale)
        parser.add_option("-t", "--t_scale", type="eng_float",
                          default=default_t_scale,
                          help="set oscope initial s/div [default=%s]" % default_t_scale)
        parser.add_option("-l", "--ref_level", type="eng_float",
                          default=default_ref_level,
                          help="set fft reference level [default=%sdB]" % default_ref_level)
        (options, args) = parser.parse_args ()
        if len(args) != 0:
            parser.print_help()
            raise SystemExit, 1

        # flow graph, including scope and fft frames
        sample_rate = int(options.sample_rate)

        # signal, noise sources need to be attributes so callbacks can get them
        self.signal = gr.sig_source_f(sample_rate, gr.GR_SIN_WAVE, options.freq,
                                    options.amplitude, 0.0)

        # Seed copied from example at cswiger/noise_source.html
        self.noise = gr.noise_source_f(options.noise_type,
                                       options.noise_amplitude,
                                       2482)
        add = gr.add_ff()
        
        throttle = gr.throttle(gr.sizeof_float, sample_rate)

        (scope_title, scope_panel, scope_vbox) = panel_info[1] #0 is ctrl panel
        scope = scopesink2.scope_sink_f(scope_panel,
                                       sample_rate=sample_rate,
                                       frame_decim=options.frame_decim,
                                       v_scale=options.v_scale,
                                       t_scale=options.t_scale)
        scope_vbox.Add (scope.win, 1, wx.EXPAND)

        fft_size = 256
        (fft_title, fft_panel, fft_vbox) = panel_info[2] # 0 is control panel
        fft = fftsink2.fft_sink_f (fft_panel,title=fft_title,
                                  fft_size=fft_size*2,
                                  sample_rate=sample_rate, baseband_freq=0,
                                  ref_level=options.ref_level,
                                  y_per_div=10)
        fft_vbox.Add (fft.win, 1, wx.EXPAND)

        self.connect (self.signal, (add,0))
        self.connect (self.noise, (add,1))
        self.connect (add, throttle)
        # self.connect (throttle, (scope, 0))
        # self.connect (throttle, (scope, 1)) # can't leave scope in unconnected
        self.connect (throttle, scope)
        self.connect (throttle, fft)

        # control panel frame
        sliders = form.form()
        
        vbox.Add((0,10), 0)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((10,0), 0)
        sliders['signal_type'] = form.static_text_field(parent=panel,sizer=hbox)
        vbox.Add(hbox, 0, wx.EXPAND)
        
        vbox.Add((0,10), 0)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((10,0), 0)
        sliders['signal_freq'] = form.slider_field(parent=panel, sizer=hbox,
                                                 label="Frequency",
                                                 weight=3,
                                                 min=0, max=2*options.freq,
                                                 callback=self.set_signal_freq)
        vbox.Add(hbox, 0, wx.EXPAND)
        
        vbox.Add((0,10), 0)
        hbox = wx.BoxSizer(wx.HORIZONTAL) # apparently you can rebind hbox
        hbox.Add((10,0), 0)
        sliders['signal_ampl'] = form.slider_field(parent=panel, sizer=hbox,
                                                 label="Amplitude",
                                                 weight=3,
                                                 min=0, max=usrp_full_scale,
                                                 callback=self.set_signal_ampl)
        vbox.Add(hbox, 0, wx.EXPAND)

        vbox.Add((0,20), 0)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((10,0), 0)
        sliders['noise_type'] = form.static_text_field(parent=panel,sizer=hbox)
        vbox.Add(hbox, 0, wx.EXPAND)

        vbox.Add((0,10), 0)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((10,0), 0)
        sliders['noise_ampl'] = form.slider_field(parent=panel, sizer=hbox,
                                                  label="Amplitude",
                                                  weight=3,
                                                  min=0, max=usrp_full_scale,
                                                  callback=self.set_noise_ampl)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.Add((0,10), 0)
        
        sliders['signal_type'].set_value("Signal: %s"
                                        % signal_string[signal_type])    
        sliders['noise_type'].set_value("Noise: %s"
                                        % noise_string[options.noise_type])
        sliders['signal_freq'].set_value(options.freq)
        sliders['signal_ampl'].set_value(options.amplitude)        
        sliders['noise_ampl'].set_value(options.noise_amplitude)

    # callbacks, these are methods in same class so callbacks can find blocks
    def set_signal_freq(self, frequency):
        self.signal.set_frequency(frequency)

    def set_signal_ampl(self, amplitude):
        self.signal.set_amplitude(amplitude)
        
    def set_noise_ampl(self, amplitude):
        self.noise.set_amplitude(amplitude)

def main ():
    app = multigui.multiapp(app_flow_graph, "SIGNAL + NOISE", nstatus=1,
                        titles=["OSCOPE", "FFT"])
    app.MainLoop()

if __name__ == '__main__':
    main ()
