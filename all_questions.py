# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = False

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since hierarchical clustering is more sensitive to local patterns in data, it is more suceptible to the affects of outliers. Since Kmeans uses averages to measure out its centroids, it is less suceptible to the influence of local outliers than agglomerative hierarchical clustering."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since the initial centroids in kmeans are randomized, it means that each run of it would have a chance to have a different result. However, since the heirarchical clustering methods are deterministic, the results will be the same no matter how many times it is run (given that the inital data and parameters are the same)."

    # type: bool (True/False)
    answers["(c)"] = False #uncertain

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While kmeans is less computationally complex than AHC, it does not mean that it is the most computationally efficient clustering algorithm out there. THere can be ceratin"

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "When the centroid is changed, the SSE may increase temporarily since some of the points in the cluster may be futher away from the new centroid than the original."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "When SSE gets smaller, it means the distance between the points in the cluster gets smaller, meaning that cohesion increases."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Since SSB indicates the deviations in means between the clusters compared to the overal data's mean, an increase in SSB would mean that the clusters are largely separated."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion would mean that the clusters become tighter, which means that separation would also improve"

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "As the kmeans algorithm progresses, the values of SSE and SSB change."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "This is not always true. At some points and datasets, increasing the cohesion of a cluster may actually decrease separation "

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "(4 * R**2) + (4 * a**2) + (4 * b**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "5 * R**2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because the centroids and points are uniformly separated, the kmeans algorithm shouldnt have any problems finding the correct cluster groups."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "While the centroids are not uniform in this example, the points in circle C should still be assigned to the right most centroid, which would pull the centroid into C. The rest of the Centroids should behave normally."

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The points in circle B will most likely be assigned to the centroid in A, meaning that the centroids in circle C will probably remain there. The centroid in A will also probably remain in that circle."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(['AB'])
    # type: explanatory string (at least four words)
    answers["(a) explain"] = "For MIN heirarchical clustering, the clusters with the shortest distance between their closest points would be considered first. In this case, it would be groups A and B."

    # type: set
    answers["(b)"] = set(['AC'])

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For MAX heirarchical clustering, the clusters with the shortest maximum distance from their members would be considered for merging. In this case, it would be groups A and C."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(['B','C','E','F','I','J','L','M'])

    # type: set
    answers["(a) boundary"] = set(['D','G'])

    # type: set
    answers["(a) noise"] = set(['A','H'])

    # type: set
    answers["(b) cluster 1"] = set(['B','C','D','E','F','G'])

    # type: set
    answers["(b) cluster 2"] = set(['I','J','L','M'])

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()
    #sqrt of 2 means that the scan reaches diagonals now.
    # type: set
    answers["(c)-a core"] = set(['B','C','D','E','F','G','I','J','L','M'])

    # type: set
    answers["(c)-a boundary"] = set(['A','H'])

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set(['A','B','C','D','E','F','G'])

    # type: set
    answers["(c)-b cluster 2"] = set(['H','I','J','L','M'])

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the most even distribution of catagories in this table."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 is almost only made up of water. Because of this, it is probably the cluster with the most clustering entropy."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Diagonal entries are comparing the distances to themselves, so will always be zero (blue)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Matrix 1 and 3 have the same pattern for red squares, but the shade of red in one is darker than that in 3. This shows that the distances between the points are greater, which corresponds to dataset Z."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Diagonal entries are comparing the distances to themselves, so will always be zero (blue)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Dataset X shows points where the distance betweeen the first and last points is red, the furthest possible. There is only one table where the red squares are in the extreme corners."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Diagonal entries are comparing the distances to themselves, so will always be zero (blue)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Similar to matrix 1, but the shade of red is lighter. This is because of the wider clusters."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "A is closest to itself, followed by B, C, and D. This corrolates with the pattern in the distance matrix."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "B is closest to itself, with the same/similar distance between B and C and being furthest from D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "C is closest to itself, with the same/similar distance between B and D and being furthest from A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "D is closest to itself, followed by C, B, and A."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchical", "overlapping", "partial"]

    # type: list
    answers["(b)"] = ["partitional", "exclusive", "complete"]

    # type: list
    answers["(c)"] = ["partitional", "exclusive", "complete"]

    # type: list
    answers["(d)"] = ["hierarchical", "overlapping", "complete"]

    # type: list
    answers["(e)"] = ["partitional", "exclusive", "partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Grades are partitioned between A-F, each student can only be in one catagory. Not every student in the computer science department has taken the class."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The inside of the circle for the first figure is too dense, which would probably create one large cluster. Figure B's interior also has a uniform spread of points, which could also lead to problems accurately clustering the different regions of interest. However, depending on the actual distance and epsilon, it could still potentially succeed."

    # type: string
    answers["(b) Figure (a)"] = "Yes"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For both examples, Kmeans could potentially assign correct clusters to the nose, face, and eyes. It would be EXTREMELY dependent on the original locations of the centroids (moreso for figure a), but would be possible for both examples ."

    # type: string
    answers["(c)"] = "Since figure a is incredibly dense apart from the shaded 'skin' region, a clustering method that can accurately create clusters for regions of low density and disregard uniform distributions of points as a factor would work best."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
