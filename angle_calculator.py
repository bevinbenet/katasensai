import math
from dataclasses import dataclass

@dataclass
class Point3D:
    x: float
    y: float 
    z: float
    
def calculate_angle(point_a : Point3D, point_b : Point3D, point_c : Point3D):
    # Create vectors from middle point
    vector_ba = [
        point_a.x - point_b.x,
        point_a.y - point_b.y, 
        point_a.z - point_b.z
    ]
    
    vector_bc = [
        point_c.x - point_b.x,
        point_c.y - point_b.y,
        point_c.z - point_b.z
    ]
    
    # Dot product
    dot_product = sum(ba * bc for ba, bc in zip(vector_ba, vector_bc))
    
    # Magnitudes
    magnitude_ba = math.sqrt(sum(x * x for x in vector_ba))
    magnitude_bc = math.sqrt(sum(x * x for x in vector_bc))
    
    # Calculate angle
    cos_angle = dot_product / (magnitude_ba * magnitude_bc)
    angle_rad = math.acos(max(-1.0, min(1.0, cos_angle)))
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg

def get_angle(df,a,b,c):
    df_angle = []
    for i in range(len(df)):
        #  if df.loc[i, f'{a}_visibility'] > 0.8 and df.loc[i, f'{b}_visibility'] > 0.8 and df.loc[i, f'{c}_visibility'] > 0.8:
        point1 = Point3D(df.loc[i, f'{a}_x'], df.loc[i, f'{a}_y'], df.loc[i, f'{a}_z'])
        point2 = Point3D(df.loc[i, f'{b}_x'], df.loc[i, f'{b}_y'], df.loc[i, f'{b}_z'])
        point3 = Point3D(df.loc[i, f'{c}_x'], df.loc[i, f'{c}_y'], df.loc[i, f'{c}_z'])
        df_angle.append(calculate_angle(point1, point2, point3))
    
    return df_angle