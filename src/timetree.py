import requests
from urllib.parse import quote
from Pairwise import Pairwise
from Timeline import Timeline
from Taxon import Taxon


def get_pairwise(taxon_id_a: int, taxon_id_b: int) -> Pairwise:
    """
    Creates a Pairwise object containining divergence data for two given taxon ids.

    :param taxon_id_a: The NCBI taxon uid for species A
    :param taxon_id_b: The NBCI taxon uid for species B
    :return: The precomputed divergence age in years
    :raises ValueError: If the API call fails or returns an invalid response
    """
    try:
        # Make the API request
        r = requests.get(
            f"http://timetree.temple.edu/api/pairwise/{taxon_id_a}/{taxon_id_b}")
        r.raise_for_status()  # Will raise an exception for HTTP errors

        # Parse the response text and extract the precomputed age
        try:
            result = Pairwise(r.text)
            return result
        except BaseException:
            raise ValueError("Parsing taxon failed. Make a Github issue.")

    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {e}")
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error processing the response: {e}")


def get_species(taxon: str) -> Taxon:
    """
    Creates a Taxon object for a given taxon name.

    :param taxon: The species name (e.g., 'Homo sapiens')
    :return: Taxon object reference
    :raises ValueError: If the API call fails or returns an invalid response
    """
    try:
        # Make the API request
        r = requests.get(
            f"http://timetree.temple.edu/api/taxon/{quote(taxon)}")
        r.raise_for_status()  # Will raise an exception for HTTP errors
        try:
            result = Taxon(r.json())
            return result
        except BaseException:
            raise ValueError("Parsing taxon failed. Make a Github issue.")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {e}")
    except (ValueError, KeyError) as e:
        raise ValueError(f"Error processing the response: {e}")


def get_timeline(taxon_id: int) -> Timeline:
    """
    Creates a Timeline object for a given taxon id. Anticipate this taking a long time.

    :param taxon_id: The NCBI taxon uid.
    :return: Timeline object reference
    :raises ValueError: If the API call fails or returns an invalid response
    """
    try:
        # Make the API request
        r = requests.get(f"http://timetree.temple.edu/api/timeline/{taxon_id}")
        r.raise_for_status()  # Will raise an exception for HTTP errors
        try:
            result = Timeline(r.text)
            return result
        except BaseException:
            raise ValueError("Parsing taxon failed. Make a Github issue.")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {e}")
    except (ValueError, KeyError) as e:
        raise ValueError(f"Error processing the response: {e}")
