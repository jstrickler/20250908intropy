import sys
import geometry  # run geometry.py and put 'geometry' in the current scope

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search order:
# 1. current folder
# 2. folders in environment variable PYTHONPATH
# 3. folders under Python installation folder (sys.prefix)

print(f"{sys.prefix = }")
for path in sys.path:
    print(path)
