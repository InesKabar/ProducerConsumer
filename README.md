# ProducerConsumer
Producer Consumer Algorithm
A Python project demonstrating the Producer-Consumer concurrency pattern using threads and a shared resource.

## Project Overview

The project implements producer and consumer threads that communicate through a shared `Boite` object.

A threading lock is used to control access to the shared resource and prevent multiple threads from modifying it at the same time.

The producer adds a value to the shared box, while the consumer retrieves values from it.

## Technologies

- Python
- Threading
- Random

## Project Structure

- `boite.py` — Shared resource used by producers and consumers.
- `producteur.py` — Producer thread that adds values to the shared resource.
- `consommateur.py` — Consumer thread that retrieves values.
- `main.py` — Main file containing the project setup.

## Key Concepts

- Multithreading
- Producer-Consumer Pattern
- Thread Synchronization
- Shared Resources
- Locks
