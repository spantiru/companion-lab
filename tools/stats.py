from typing import Set, Any
from dataclasses import dataclass

def probability(A: Set[Any], omega: Set[Any]):
    """ Probability for a uniform distribution
    in a finite space"""
    return len(A) / len(omega)


@dataclass(frozen=True)
class WeightedOutcome:
    """ Class adding a weight to any outcome. """
    weight: float


def probability_weighted(A: Set[WeightedOutcome], 
                         omega: Set[WeightedOutcome]):
    """ Probability for a uniform distribution
    in a finite space. Omega is defined as a dictionary with 
    values being weights. """
    A_weight = sum((o.weight for o in A))
    omega_weight = sum((o.weight for o in omega))
    return A_weight / omega_weight