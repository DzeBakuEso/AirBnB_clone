# AirBnB Clone Project

The AirBnB clone project is an ongoing journey to create a simplified version of the AirBnB web application. The main objective is to build an interactive web application with essential features while learning key programming concepts, including object-oriented programming, file storage, testing, and APIs.

## Table of Contents
- [Project Structure](#project-structure)
- [Concepts to Learn](#concepts-to-learn)
- [Steps](#steps)
- [Files and Directories](#files-and-directories)
- [Storage and Persistence](#storage-and-persistence)
- [Serialization/Deserialization](#serializationdeserialization)
- [Using *args and **kwargs](#using-args-and-kwargs)
- [Working with Datetime](#working-with-datetime)
- [Testing](#testing)

## Project Structure

### Directory Overview

- **models/**: Contains all classes that represent data objects.
  - `base_model.py`: The base class for all models, containing common attributes and methods (`id`, `created_at`, `updated_at`, `save()`, `to_json()`).
  - **engine/**: Includes storage-related classes, starting with `file_storage.py`, which manages the persistence layer (saving and loading data to/from files).
  
- **tests/**: Contains all unit tests for the project.
  
- **console.py**: The entry point for the command interpreter (CLI). This is where you interact with your application through the terminal, testing commands to manipulate objects.

### Key Files

- `models/base_model.py`: Defines the `BaseModel` class with basic object attributes like `id`, `created_at`, `updated_at`, and methods for saving and serializing objects.
- `models/engine/file_storage.py`: The file storage engine used to persist your objects in a JSON format.
- `console.py`: The command-line interface that allows interaction with your objects, enabling users to create, update, delete, and view objects.

## Concepts to Learn

### Unittest
- Learn how to write unit tests for your application to ensure your code is working as expected.

### Python Packages Concept
- Understand how to organize and manage your Python code into reusable packages.

### Serialization/Deserialization
- Learn how to convert your objects into a format that can be saved (JSON) and later restored.

### *args, **kwargs
- Learn how to pass a variable number of arguments to functions using `*args` and `**kwargs`.

### Datetime
- Understand how to manipulate and format dates and times using Python's `datetime` module.

## Steps

The project is divided into several stages, each corresponding to a concept. You will complete them step by step, with each stage focusing on a specific concept.

### Steps Overview:

1. **Command Interpreter**: Create a command-line interface for interacting with the program.
2. **Data Models**: Define your models (e.g., `BaseModel`) and attributes (`id`, `created_at`, `updated_at`).
3. **Managing Objects**: Implement methods to create, update, and delete objects through the console.
4. **File Storage**: Save your objects to a JSON file and load them back on subsequent executions.
5. **Abstraction**: Ensure your models can work with different types of storage systems (file, database, etc.) without changing the codebase.
6. **Web Front-End & API**: Create a simple front-end and API to interact with the objects.

## Files and Directories

### Directory Structure


### File Descriptions

- **models/**: This directory contains all the classes used throughout the project. It follows the object-oriented principles.
  - `base_model.py`: The base class from which all other models will inherit.
  
- **tests/**: This folder includes unit tests to ensure your models and other components are functioning correctly.

- **console.py**: The entry point for the command interpreter. You can use this to interact with the objects in your application.

- **models/engine/file_storage.py**: Contains methods to save and load your objects to/from a file (JSON format).

## Storage and Persistence

Persistence ensures that your objects remain saved between program executions. This project initially focuses on file-based storage.

### File Storage (JSON Serialization)

- **Serialization**: Convert objects to JSON format, so they can be saved to a file.
- **Deserialization**: Read the JSON file, parse it, and recreate the objects when the program starts again.

### Why Use JSON?
JSON is a widely-used format that allows your objects to be easily saved, read, and shared across different programming languages. It’s both human-readable and machine-readable.

### Save & Load Process:
1. **Save**: Convert an object to a dictionary using `to_json()`, then serialize it using `json.dumps()` and save to a file.
2. **Load**: Read the JSON file, convert the string back to a dictionary with `json.loads()`, and use that to recreate your objects.

## Serialization/Deserialization

- **Serialization**: Convert Python objects (e.g., instances of `BaseModel`) to a dictionary representation, which can be easily converted into a JSON string using `json.dumps()`.
- **Deserialization**: Read the JSON file, convert it back into a dictionary, and use that data to recreate objects.

```python
import json

# Example: Serialize object to file
obj_dict = obj.to_json()
with open("storage.json", "w") as f:
    json.dump(obj_dict, f)

# Example: Deserialize object from file
with open("storage.json", "r") as f:
    data = json.load(f)
obj = MyModel(data)

