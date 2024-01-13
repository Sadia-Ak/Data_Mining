def edit_distance(s1, s2):
    # Create a matrix to store the distances
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the matrix
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    # Fill in the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    return matrix[len(s1)][len(s2)]

# Example 1
sString1 = "kitten"
sString2 = "sitting"
distance1 = edit_distance(sString1, sString2)
print(f"Example 1 Output: Edit distance between '{sString1}' and '{sString2}' is {distance1}")

# Example 2
sString1 = "GAMBOL"
sString2 = "GUMBO"
distance2 = edit_distance(sString1, sString2)
print(f"Example 2 Output: Edit distance between '{sString1}' and '{sString2}' is {distance2}")
