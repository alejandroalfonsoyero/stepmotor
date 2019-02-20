#!/usr/bin/env python3
# -*- coding: utf-8 -*-

state0 = 0
state1 = 1
state2 = 2
state3 = 3


class StepMotorController:
    def __init__(self,
                 motor_id,
                 port_controller,
                 angle_step,
                 long_revol,
                 control_pins,
                 limit,
                 start_pos=0):
        self.id = motor_id
        self.port_controller = port_controller
        self.angle_step = angle_step
        self.long_revol = long_revol
        self.control_pins = control_pins
        self.limit = limit
        self.position = start_pos
        self.long_step = long_revol * angle_step / 360
        self.precision = self.long_step / 2
        self.state = state0
        if len(self.control_pins) == 2:
            self.port_controller.setDataPin(self.control_pins[0], True)
            self.port_controller.setDataPin(self.control_pins[1], True)

	#Motor unipolar
    def f_step(self):
        if len(self.control_pins) == 2:
            if self.state == state0:
                self.state = state1
                #primer paso
                self.port_controller.setDataPin(self.control_pins[1], False)
            elif self.state == state1:
                self.state = state2
                #segundo paso
                self.port_controller.setDataPin(self.control_pins[0], False)
            elif self.state == state2:
                self.state = state3
                #tercer paso
                self.port_controller.setDataPin(self.control_pins[1], True)
            elif self.state == state3:
                self.state = state0
                #cuarto paso
                self.port_controller.setDataPin(self.control_pins[0], True)

    #Motor unipolar
    def b_step(self):
        if len(self.control_pins) == 2:
            if self.state == state0:
                self.state = state3
                #primer paso
                self.port_controller.setDataPin(self.control_pins[0], False)
            elif self.state == state3:
                self.state = state2
                #segundo paso
                self.port_controller.setDataPin(self.control_pins[1], False)
            elif self.state == state2:
                self.state = state1
				#tercer paso
                self.port_controller.setDataPin(self.control_pins[0], True)
            elif self.state == state1:
                self.state = state0
                #cuarto paso
                self.port_controller.setDataPin(self.control_pins[1], True)
