#include <stdio.h>
#include <string.h>

#define rep(i, N) for (int i = 0; i < N; i++)

typedef struct {
	int size;
	int elem[5];
} vector;

typedef struct {
	int value;
	char terminal;
} int_with_terminal;

int_with_terminal expr_int(int *);
vector expr_vector(vector *, int *);
vector get_vector(vector *, int *);

int main() {
	int N;
	scanf("%d", &N);
	int int__[128] = {0};
	rep(i, 10) { int__[i + '0'] = i; }
	vector vec__[128];
	char *statement__[4] = {"int", "print_int", "vec", "print_vec"};
	rep(i, N) {
		char statement[9];
		scanf("%s", statement);
		if (strcmp(statement, statement__[0]) == 0) {
			char var_name;
			scanf(" %c %*c", &var_name);
			int__[var_name] = expr_int(int__).value;
		} else if (strcmp(statement, statement__[1]) == 0) {
			printf("%d\n", expr_int(int__).value);
		} else if (strcmp(statement, statement__[2]) == 0) {
			char var_name;
			scanf(" %c %*c", &var_name);
			vec__[var_name] = expr_vector(vec__, int__);
		} else if (strcmp(statement, statement__[3]) == 0) {
			vector vec = expr_vector(vec__, int__);
			printf("[");
			rep(i, vec.size) { printf(" %d", vec.elem[i]); }
			printf(" ]\n");
		}
	}
}

int_with_terminal expr_int(int *int__) {
	int_with_terminal result;
	char op_buf, val_buf;
	scanf(" %c", &val_buf);
	result.value = int__[val_buf];
	while (1) {
		scanf(" %c", &op_buf);
		if (op_buf == ';' || op_buf == ',' || op_buf == ']') {
			result.terminal = op_buf;
			break;
		}
		scanf(" %c", &val_buf);
		result.value += op_buf == '+' ? int__[val_buf] : -int__[val_buf];
	}
	return result;
}

vector expr_vector(vector *vec__, int *int__) {
	vector vec, vec_buf;
	char buf;
	vec = get_vector(vec__, int__);
	while (1) {
		scanf(" %c", &buf);
		if (buf == ';') {
			break;
		}
		vec_buf = get_vector(vec__, int__);
		rep(i, vec.size) {
			vec.elem[i] += buf == '+' ? vec_buf.elem[i] : -vec_buf.elem[i];
		}
	}
	return vec;
}

vector get_vector(vector *vec__, int *int__) {
	char buf;
	scanf(" %c", &buf);
	if (buf == '[') {
		vector vec = {.size = 0};
		for (int i = 0;; i++) {
			int_with_terminal elem = expr_int(int__);
			vec.size++;
			vec.elem[i] = elem.value;
			if (elem.terminal == ']') {
				break;
			}
		}
		return vec;
	} else {
		return vec__[buf];
	}
}
