# ROS2-STM32 Brake-by-Wire Controller

## Overview

This project demonstrates a brake-by-wire control system integrating ROS2 and an STM32 microcontroller.

A ROS2 node running on a host computer publishes brake actuation commands over UART. The STM32 receives these commands using an interrupt-driven UART interface, processes the incoming data, and generates PWM signals to control a 12V electromechanical brake actuator capable of producing up to 150N of force.

The project was developed to gain hands-on experience with embedded firmware development, UART communication, hardware timers, PWM generation, and ROS2 integration for real-time actuator control applications.

---

## System Architecture

```text
+--------------------+
|      ROS2 Node     |
+--------------------+
           |
           | UART (115200 Baud)
           |
           v
+--------------------+
|      STM32F4       |
| Interrupt-Driven   |
| UART Reception     |
+--------------------+
           |
           | PWM Output
           |
           v
+--------------------+
| 12V Brake Actuator |
|     150N Force     |
+--------------------+
           |
           v
+--------------------+
| Brake Mechanism    |
+--------------------+
```

---

## Features

* ROS2-to-STM32 communication over UART
* Interrupt-driven UART reception
* Real-time command processing
* Hardware PWM generation using TIM2
* Brake actuator control
* Lightweight communication protocol
* Modular firmware architecture

---

## Hardware

### Microcontroller

* STM32F4 Series MCU

### Actuator

* 12V Electromechanical Brake Actuator
* Rated Force: 150N

### Peripherals Used

* USART2
* TIM2 Channel 1
* GPIO Alternate Function

---

## Software Stack

### Host Side

* ROS2
* Python

### Embedded Side

* STM32 HAL
* STM32CubeMX
* STM32CubeIDE

---

## Communication Protocol

The ROS2 node transmits a 3-byte ASCII command representing the desired actuator position.

### Example Commands

| Command | Value                 |
| ------- | --------------------- |
| 000     | Minimum Position      |
| 045     | Intermediate Position |
| 090     | Intermediate Position |
| 135     | Intermediate Position |
| 180     | Maximum Position      |

Example:

```text
090
```

The STM32 receives the command, converts the ASCII data into an integer value, and updates the PWM duty cycle accordingly.

---

## Firmware Workflow

1. Initialize system clock and peripherals.
2. Configure USART2 for interrupt-based reception.
3. Configure TIM2 for PWM generation.
4. Wait for incoming UART commands.
5. Parse received actuator command.
6. Update PWM compare register.
7. Generate PWM output for actuator control.

---

## Repository Structure

```text
.
├── ros2_node/
│   └── ROS2 source code
│
├── stm32_firmware/
│   ├── Core/
│   ├── Drivers/
│   ├── *.ioc
│   └── STM32CubeIDE project
│
└── README.md
```

---

## Embedded Systems Concepts Demonstrated

* UART Communication
* Interrupt Service Routines (ISR)
* Hardware Timers
* PWM Signal Generation
* Embedded Firmware Development
* Peripheral Configuration
* Real-Time Control
* Host-to-Microcontroller Communication
* Brake-by-Wire Actuation

---

## Future Improvements

* FreeRTOS Integration
* CRC Error Detection
* Closed-Loop Position Control
* Encoder Feedback Integration
* Safety Monitoring and Fault Handling

---

## Learning Outcomes

This project provided practical experience with:

* STM32 peripheral configuration
* Interrupt-driven firmware design
* Hardware PWM generation
* Serial communication protocols
* ROS2 and embedded system integration
* Real-time actuator control
* Embedded software architecture

---

## Author

Kevin Dsouza

Embedded Systems | Firmware Development | Robotics

