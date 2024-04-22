import math

#Function to load the coordinates from a file path
def load_coordinates(path):
  coordinates = []
  with open(path,'r') as file:
    for line in file:
      x,y = map(int,line.strip().split(','))
      coordinates.append((x,y))
  return coordinates

#Function that checks if the points form a rectangle
def is_rectangle(point_A,point_B,point_C):
  #It does this by using the Euclid distance formula of each pair points of A,B,C and then stores them in
  #a list called distances
  distances = [
    pow((point_B[0] - point_A[0]),2) + pow((point_B[1] - point_A[1]),2),
    pow((point_C[0] - point_B[0]),2) + pow((point_C[1] - point_B[1]),2),
    pow((point_A[0] - point_C[0]),2) + pow((point_A[1] - point_C[1]),2)
  ] 
  #It then sorts the distances in ascending order. This is to ensure the shortest distances are
  #at the start of the list while the longest is at the end of the list
  distances.sort()
  #It checks if the sum of the two shorter distances is equal to the square of the longest distance
  return distances[0] + distances[1] == distances[2]

#Function to see if the point X is inside the object
def is_point_inside(point_A,point_B,point_C,point_X):
  #It does this by calculating the min and the max of the x and y coordinates of the object
  min_x = min(point_A[0],point_B[0],point_C[0])
  max_x = max(point_A[0],point_B[0],point_C[0])
  min_y = min(point_A[1],point_B[1],point_C[1])
  max_y = max(point_A[1],point_B[1],point_C[1])

  #And the checks of point X falls within the range of the min and max values of the x,y coordinates of the object
  return min_x <= point_X[0] <= max_x and min_y <= point_X[1] <= max_y

#Function to calculate the diagonal of the rectangle. Point C is optional.
def calculate_diagonal(point_A,point_B,point_c = 0):
  #It does this by using the Euclid distance formula 
  return math.sqrt(pow((point_B[0] - point_A[0]),2) + pow((point_B[1] - point_A[1]),2))

#Main function of the app
def main():
  path_to_coordinates = "./coordinates/coordinates.txt" 

  coordinates = load_coordinates(path_to_coordinates) 

  point_A,point_B,point_C,point_X = coordinates 

  try:
    if not is_rectangle(point_A,point_B,point_C):
      raise ValueError("Dobivene točke nemogu biti vrhovi pravokutnika!")
  except ValueError as error:
    print(f"Greška:{error}")
    return

  is_inside = is_point_inside(point_A,point_B,point_C,point_X)

  print("Izlaz:")
  if is_inside:
    print("True")
  else:
    print("False")
  
  diagonal = calculate_diagonal(point_A,point_B,point_C)




if __name__ == "__main__":
  main()