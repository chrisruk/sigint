#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class sig(gr.sync_block):
    """
    docstring for block sig
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="sig",
            in_sig=[(numpy.complex64,1024*5)],
            #in_sig=[(numpy.float32,1024)],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items
        #print("Max",numpy.max(in0))
        #print((numpy.amax(numpy.abs(in0))**2)/1024)
    
        print(numpy.amax(numpy.abs(in0)))
        # <+signal processing here+>
        return 1#len(input_items[0])

