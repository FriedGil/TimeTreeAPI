from typing import List, Dict, Optional


class Taxon:
    """
    A class to represent a taxon (organism) in a taxonomic study.

    This class encapsulates data related to a taxon, including its identifiers,
    scientific name, taxonomic rank, study times, and related studies.

    Attributes:
    taxon_id (int): The unique identifier for the taxon.
    c_syn_type (str): The synonym type associated with the taxon.
    c_syn_name (str): The synonym name associated with the taxon.
    scientific_name (str): The scientific name of the taxon.
    topology_node_id (int): The identifier for the topology node.
    taxonomic_rank (str): The taxonomic rank of the taxon (e.g., species, genus).
    study_times (List[Dict]): A list of study time data associated with the taxon.
    study_time_estimate (Optional[float]): The estimated study time for the taxon, extracted from the study times.
    studies (List[Dict]): A list of studies related to the taxon.
    is_leaf (Optional[bool]): Indicates whether the taxon is a leaf in the taxonomic tree.
    any_id (int): A generic identifier associated with the taxon.
    timetree_id (int): The identifier for the timetree associated with the taxon.
    ncbi_id (int): The NCBI identifier for the taxon.
    rank_this (Optional[Dict]): The current rank information of the taxon.
    rank_less_specific (List[Dict]): A list of less specific ranks in the taxonomic hierarchy.
    rank_more_specific (List[Dict]): A list of more specific ranks in the taxonomic hierarchy.
    is_leaf_bool (bool): A boolean indicating whether the taxon is a leaf.
    """

    def __init__(self, data: Dict):
        self.json = data
        self.taxon_id: int = data.get("taxon_id")
        self.c_syn_type: str = data.get("c_syn_type")
        self.c_syn_name: str = data.get("c_syn_name")
        self.scientific_name: str = data.get("scientific_name")
        self.topology_node_id: int = data.get("topology_node_id")
        self.taxonomic_rank: str = data.get("taxonomic_rank")

        # 'study_times' is a list of dictionaries; extracting the 'f_time_estimate' as a float
        self.study_times: List[Dict] = data.get("study_times", [])
        self.study_time_estimate: Optional[float] = (
            float(self.study_times[0].get("f_time_estimate"))
            if self.study_times
            else None
        )

        self.studies: List[Dict] = data.get("studies", [])
        self.is_leaf: Optional[bool] = data.get("is_leaf")
        self.any_id: int = data.get("any_id")
        self.timetree_id: int = data.get("timetree_id")
        self.ncbi_id: int = data.get("ncbi_id")

        # Handling the 'rank' field, which is a nested dictionary
        rank_data = data.get("rank", {})
        self.rank_this: Optional[Dict] = rank_data.get("this")
        self.rank_less_specific: List[Dict] = rank_data.get("lessSpecific", [])
        self.rank_more_specific: List[Dict] = rank_data.get("moreSpecific", [])

        self.is_leaf_bool: bool = data.get("isLeaf", False)

    def __repr__(self):
        return (
            f"Taxon(taxon_id={
                self.taxon_id}, c_syn_name={
                self.c_syn_name}, " f"scientific_name={
                self.scientific_name}, taxonomic_rank={
                    self.taxonomic_rank}, " f"study_time_estimate={
                        self.study_time_estimate}, is_leaf={
                            self.is_leaf_bool})")
