def get_stats(non_unique_list):
	answer = {}
	unique_list = list(set(non_unique_list))
	digits = [0 for _ in unique_list]
	for i in range(len(non_unique_list)):
		for j in range(len(unique_list)):
			a = unique_list[j]
			if non_unique_list[i] == a:
				digits[unique_list.index(a)] += 1
	for k in range(len(digits)):
		answer.update({unique_list[k]: digits[k]})
	return answer


def sort_dict(input_dict):
	return sorted(([v, k] for k, v in input_dict.iteritems()), reverse=True)
