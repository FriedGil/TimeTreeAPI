# TimeTreeAPI

## Overview

TimeTreeAPI is a Python library designed to interact with the TimeTree API, providing tools for working with taxonomic data, divergence times, and evolutionary studies. The library includes classes and functions to process API responses, enabling seamless integration into taxonomic and evolutionary research workflows.

---
## Installation

```bash
pip install timetreeapi
```

## Usage
```python
import timetree

human_chimp_pw = get_pairwise(get_taxon("Homo sapiens").taxon_id, get_taxon("Pan troglodytes").taxon_id)
print(human_chimp_pw.precomputed_age)
chordata_timeline = get_timeline(get_taxon("Chordata"))
print(chordata_timeline.get_taxa_by_rank('family'))
```
## Features

- **Pairwise:** Handles pairwise taxon comparison data, including divergence estimates and confidence intervals.
- **Taxon:** Represents individual taxonomic entities with detailed attributes and relationships.
- **Timeline:** Processes and analyzes CSV data from TimeTree, including filtering methods based on rank or taxonomic level.
- **API Functions:**
  - Fetch pairwise divergence data for two species.
  - Retrieve detailed taxonomic information for a given species.
  - Extract timeline data for a specified taxon.

---

