HEADER = "template <typename T>\nconstexpr auto flatten_impl(const T& t, std::integral_constant<std::size_t, 0> N1) noexcept {\n"
index = HEADER.find('0')
def gen_head(num):
  return HEADER[:index] + str(num) + HEADER[index+1:]
def gen_seq(num):
  seq = ""
  for i in range(1, num+1):
    if i>1:
      seq += ", "
    seq += 'f' + str(i)
  return seq
def gen_bind(num):
  if num==0:
    return ""
  else:
    return "  auto& [" + gen_seq(num) + "] = t;\n"
def gen_return(num):
  return "  return std::forward_as_tuple(" + gen_seq(num) + ");\n}"

def gen(num):
  return gen_head(num) + gen_bind(num) + gen_return(num);

if __name__ == "__main__":
  import sys
  if len(sys.argv)!=2:
    print("please input the number for gen() correctly!")
  else:
    for i in range(int(sys.argv[1]) + 1):
      print(gen(i))