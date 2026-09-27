# Music Intelligence Lab
## Development Log

### Milestone 1: Initial Prototype

- Built initial Python playlist analysis script.
- Implemented artist and genre frequency analysis.
- Added oldest-song detection.
- Established CSV as the initial data source.

### Milestone 2: Database Layer

- Introduced SQLite for persistent song storage.
- Separated database connection, schema, and query logic.
- Implemented SQL aggregations for:
  - genre frequency
  - artist frequency
  - average rating
  - oldest/newest songs
  - top-rated songs

### Milestone 3: Modular Architecture

- Separated analysis logic into `analysis_service.py`.
- Separated data loading into `data_service.py`.
- Separated database responsibilities into:
  - `connection.py`
  - `models.py`
  - `queries.py`

### Milestone 4: Pandas Integration

- Introduced Pandas DataFrames for analytical processing.
- Migrated genre analysis to Pandas.
- Migrated artist analysis to Pandas.
- Migrated year analysis to Pandas.
- Added average rating analysis.
- Added year-frequency analysis.