#Given a list of score [45, 78, 92, 23, 67], normalize to 0-1 using min-max scaling wit loops

scores = [45, 78, 92, 23, 67]

min_val = scores[0]
max_val = scores[0]

#Find min and max using loops

for i in scores:
    if i < min_val:
        min_val = i
        if i> max_val:
            max_val=i

            #Normalize values
            normalized = []
            for i in scores:
                norm = (i - min_val)/(max_val-min_val)
                normalized.append(norm)

                print("Original:", scores)
                print("Normalized:", normalized)