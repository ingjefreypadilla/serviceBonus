## ADR N: First Contact

### Context
To ascertain the precise value of the calculated bonus, it is imperative to consolidate all business logic into a singular use case.    

### Decision
I have developed a layer to encapsulate all business logic within a straightforward case use. This design enables the infrastructure layer CLI to provide the worker parameters, and the layer will subsequently deliver the results in a straightforward manner.

### Consequences
This structure enables us to share the same functionality with another layer, such as an API, and others.