class Pairwise:
    """
    A class to represent pairwise taxon data.

    This class processes a raw string of comma-separated data, fixing malformed API output
    and extracting relevant fields into corresponding attributes for pairwise taxon comparisons.

    Attributes:
    taxon_a_id (int): The identifier for taxon A.
    taxon_b_id (int): The identifier for taxon B.
    scientific_name_a (str): The scientific name of taxon A.
    scientific_name_b (str): The scientific name of taxon B.
    all_total (float): The total value for the pairwise comparison.
    precomputed_age (float): The precomputed age estimate for the pair.
    precomputed_ci_low (float): The lower bound of the precomputed confidence interval.
    precomputed_ci_high (float): The upper bound of the precomputed confidence interval.
    adjusted_age (float): The adjusted age estimate for the pair.
    """

    def __init__(self, data: str):
        self.data: str = data
        fixed_data = data.replace("\r", ",").replace(
            "\n", ","
        )  # API output data is malformed, this fixes it.
        fields = fixed_data.split(",")
        self.taxon_a_id: int = int(fields[10])
        self.taxon_b_id: int = int(fields[11])
        self.scientific_name_a: str = fields[12]
        self.scientific_name_b: str = fields[13]
        self.all_total: float = float(fields[14])
        self.precomputed_age: float = float(fields[15])
        self.precomputed_ci_low: float = float(fields[16])
        self.precomputed_ci_high: float = float(fields[17])
        self.adjusted_age: float = float(fields[18])

    def __repr__(self) -> str:
        return (
            f"Pairwise(taxon_a_id={
                self.taxon_a_id}, taxon_b_id={
                self.taxon_b_id}, " f"scientific_name_a='{
                self.scientific_name_a}', scientific_name_b='{
                    self.scientific_name_b}', " f"all_total={
                        self.all_total}, precomputed_age={
                            self.precomputed_age}, " f"precomputed_ci_low={
                                self.precomputed_ci_low}, precomputed_ci_high={
                                    self.precomputed_ci_high}, " f"adjusted_age={
                                        self.adjusted_age})")
