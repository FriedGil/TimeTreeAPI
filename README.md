# TimeTree API Integration

This project provides Python functions to interact with the TimeTree API. TimeTree is an online database of species divergence times based on molecular data. The project includes functions to retrieve pairwise divergence data, species-specific data, and timelines for evolutionary history.

## Features

- **Get Pairwise Divergence**: Fetches divergence data between two species using their NCBI taxon IDs.
- **Get Species Data**: Retrieves species-specific information based on the species name.
- **Get Timeline Data**: Fetches a timeline of evolutionary events for a given species ID.

## Requirements

- `requests` library
- `pandas` library

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

   ```bash
   pip install timetreeapi
