# TimeTreeAPI

[GitHub Repository](https://github.com/FriedGil/TimeTreeAPI)

## Overview

TimeTreeAPI is a Python library designed to interact with the TimeTree API, providing tools for working with taxonomic data, divergence times, and evolutionary studies. The library includes classes and functions to process API responses, enabling seamless integration into taxonomic and evolutionary research workflows.

---

## Features

- **Pairwise:** Handles pairwise taxon comparison data, including divergence estimates and confidence intervals.
- **Taxon:** Represents individual taxonomic entities with detailed attributes and relationships.
- **Timeline:** Processes and analyzes CSV data from TimeTree, including filtering methods based on rank or taxonomic level.
- **API Functions:**
  - Fetch pairwise divergence data for two species.
  - Retrieve detailed taxonomic information for a given species.
  - Extract timeline data for a specified taxon.

---

## Installation

```bash
pip install timetreeapi
```

## Usage

### Pairwise Class

The `Pairwise` class processes raw API output to provide structured data for pairwise taxonomic comparisons.

#### Attributes
- `taxon_a_id` and `taxon_b_id`: IDs of the two taxa.
- `scientific_name_a` and `scientific_name_b`: Scientific names of the taxa.
- `all_total`, `precomputed_age`, `precomputed_ci_low`, `precomputed_ci_high`, and `adjusted_age`: Various age metrics.