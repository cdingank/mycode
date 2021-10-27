
#!/usr/bin/env python3
students = [{"name": "Steve", "score": 88}, {"name": "Becky", "score": 99}, {"name": "Chad", "score": 76}]


	# And print out each of the students' names, scores, and grade they would receive (90-100 A, 80-90 B, etc)
	# "Steve got a(n) 88, so this student received a(n) B


for x in students:
    y = x['name']
    z = x['score']
    g = ""
    if z > 89:
        g = 'A'
    elif z > 79:
        g = 'B'
    else: 
        g = 'C'
    print(f"{y} got a(n) {z}, so his grade is {g}")
