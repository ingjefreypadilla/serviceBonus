## ADR N: First Contact

### Context
As an integral component of this solution, it is imperative to ascertain the number of worked days.     

### Decision
At this juncture, I have come to the realization that the starting date for receiving the parameters is not consistent for unpaid days. Consequently, it is imperative to validate the input in the infrastructure layer, ensuring that the dates are validated within the same year.

### Consequences
We must verify with the business whether this rule is appropriate or if it should be interpreted differently in such cases.
