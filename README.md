# AI Companion (Raspberry Pi)

A small standalone **AI desk companion** powered by a Raspberry Pi.
The device runs a **local LLM**, displays information on a **16x2 I2C LCD**, and behaves like a tiny retro AI terminal.

The goal of this project is to build a **low-cost, self-contained AI device** with personality — inspired by retro computers and small assistant devices.

---

## Features

* Runs a **local LLM** directly on the Raspberry Pi
* Displays messages and animations on a **16x2 I2C LCD**
* Minimal terminal-style interface
* Local memory / knowledge retrieval
* Lightweight design using Raspberry Pi OS Lite
* Offline capable

---

## Hardware

Main device:

* Raspberry Pi 4 Model B
* 16x2 I2C LCD display (HD44780 compatible)
* MicroSD card
* 5V 3A power supply
* Small cooling fan (CanaKit case)

LCD wiring:

| LCD | Raspberry Pi |
| --- | ------------ |
| VCC | 5V           |
| GND | GND          |
| SDA | GPIO2        |
| SCL | GPIO3        |

---

## Software Stack

* Raspberry Pi OS Lite
* Python
* llama.cpp (for local LLM inference)
* TinyLlama 1.1B (quantized model)
* RPLCD (LCD control library)

---

## Project Structure

```
ai-companion/
│
├── src/
│   ├── lcd_controller.py
│   ├── chatbot.py
│
├── brain/
│   └── memory.txt
│
├── models/
│   └── tinyllama.gguf
│
├── lcd_test.py
├── requirements.txt
└── README.md
```

---

## Setup

Clone the repository:

```
git clone https://github.com/<your-username>/ai-companion.git
cd ai-companion
```

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## LCD Test

Run the LCD test script:

```
python lcd_test.py
```

Expected output on the LCD:

```
Hello
AI Booting (o_o)
```

---

## Running the Companion

(Work in progress)

Eventually the device will:

1. Boot the Raspberry Pi
2. Launch the chatbot automatically
3. Accept user input
4. Generate responses using a local LLM
5. Display responses on the LCD

---

## Roadmap

* LCD UI system
* Local LLM integration
* Retrieval-based memory system
* Boot-time auto-launch
* Voice interaction
* Animated LCD expressions

---

## Inspiration

This project is inspired by small AI gadgets and retro computing aesthetics — the goal is to build something that feels like a **tiny physical AI assistant** rather than a traditional computer.


