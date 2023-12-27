import numpy as np
t = np.array([4,11])
vw = np.array([[1,2], [3,5]])

print("\nMatrix vw",vw, "\nVector t:",t,sep="\n")


def check_vector_span(set_of_vectors, vector_to_check):
    # Creates an empty vector of correct size
    vector_of_scalars = np.asarray([None] * set_of_vectors.shape[0])

    # Solves for the scalars that make the equation true if the vector is within the span
    try:
        # Use np.linalg.solve() function to solve for vector_of_scalars
        vector_of_scalars = np.linalg.solve(set_of_vectors, vector_to_check)
        if not (vector_of_scalars is None):
            print("\nVector is within span.\nScalars in s:", vector_of_scalars)
    # Handles the cases when the vector is NOT within the span
    except Exception as exception_type:
        if str(exception_type) == "Singular matrix":
            print("\nNo single solution\nVector is NOT within span")
        else:
            print("\nUnexpected Exception Error:", exception_type)
    return vector_of_scalars


# Example usage:
# Define a set of vectors and a vector to check if it's within the span
set_of_vectors = np.array([[2, 1], [3, 2]])
vector_to_check = np.array([5, 4])

# Call the function
check_vector_span(set_of_vectors, vector_to_check)

