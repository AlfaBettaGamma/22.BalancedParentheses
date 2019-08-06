def recParenthese(output, open, close, N,res):
  if open == N and close == N:
    res.append(output)
  else:
    if open < N:
      recParenthese(output + '(', open + 1, close, N,res)
    if close<open:
      recParenthese(output + ')', open, close + 1, N,res)
  return res


def BalancedParentheses(N):
  res = []
  result = ''
  res = recParenthese('', 0, 0, N,res)
  result = ' '.join(res)
  return result