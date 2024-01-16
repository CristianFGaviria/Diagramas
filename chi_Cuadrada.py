def media(X):
  return sum(X) / len(X)


def varianza(X):
  promedio = media(X)
  promedio = round(promedio, 9)
  print(f'El promedio es = {promedio}')

  acumulado = 0
  for x in X:
    acumulado += (x - promedio)**2

  return acumulado / (len(X) - 1)



def limite_superior_varianza(alpha, n):
  chi_cuadrada = float(input("Ingrese el valor de Chi cuadrada segun los resultados de 1-(a/2) y n-1 (LIMITE SUPERIOR) : ")) # 74.2219
  return chi_cuadrada / (12 * (n - 1))



def limite_inferior_varianza(alpha, n):
  print(f'El valor de n es = {n}')
  chi_cuadrada = float(input("Ingrese el valor de Chi cuadrada segun los resultados de (a/2) y n-1 (LIMITE INFERIOR) : ")) # 129.5613
  return chi_cuadrada / (12 * (n - 1))



def prueba_varianza(alpha, X):

  alpha = round(alpha,3)
  print(f'El valor de a es = {alpha}')
  a = 1 - alpha + alpha / 2
  print(f'El valor de 1-(a/2) es = {a}')
  b = alpha / 2
  print(f'El valor de (a/2) es = {b}')
  var_x = varianza(X)

  li_varianza = limite_inferior_varianza(alpha, len(X))
  li_varianza = round(li_varianza, 9)
  print(f'El valor del limite inferior de la VARIANZA es: {li_varianza}')
  ls_varianza = limite_superior_varianza(alpha, len(X))
  ls_varianza = round(ls_varianza, 9)
  print(f'El valor del limite superior de la VARIANZA es: {ls_varianza}')

  if ls_varianza <= var_x <= li_varianza:
    print(
      f'El valor promedio de V(r) = {var_x}  se encuentra entre los limites aceptables')
  else:
    print(
      f'El valor promedio de V(r) = {var_x} no se encuentra entre los limites aceptables')




if __name__ == '__main__':
  X = [
    0.690721649, 0.144329897, 0.412371134, 0.75257732, 0.453608247,
    0.865979381, 0.113402062, 0.18556701, 0.618556701, 0.783505155,
    0.608247423, 0.731958763, 0.216494845, 0.907216495, 0.567010309,
    0.525773196, 0.319587629, 0.288659794, 0.134020619, 0.278350515,
    0.164948454, 0.340206186, 0.391752577, 0.649484536, 0.93814433,
    0.381443299, 0.701030928, 0.092783505, 0.12371134, 0.309278351,
    0.237113402, 0.87628866, 0.072164948, 0.422680412, 0.432989691,
    0.257731959, 0.979381443, 0.587628866, 0.628865979, 0.835051546,
    0.484536082, 0.793814433, 0.226804124, 0.824742268, 0.81443299,
    0.762886598, 0.505154639, 0.443298969, 0.556701031, 0.515463918,
    0.268041237, 0.030927835, 0.845360825, 0.917525773, 0.494845361,
    0.103092784, 0.154639175, 0.463917526, 0.010309278, 0.742268041,
    0.402061856, 0.680412371, 0.670103093, 0.855670103, 0.969072165,
    0.536082474, 0.371134021, 0.546391753, 0.948453608, 0.711340206,
    0.659793814, 0.989690722, 0.639175258, 0.886597938, 0.958762887,
    0.020618557, 0.474226804, 0.06185567, 0, 0.690721649, 0.350515464,
    0.773195876, 0.206185567, 0.721649485, 0.298969072, 0.18556701,
    0.360824742, 0.082474227, 0.041237113, 0.896907216, 0.175257732,
    0.567010309, 0.597938144, 0.195876289, 0.24742268, 0.927835052,
    0.329896907, 0.340206186, 0.051546392, 0.804123711
  ]
  aceptacion = int(input("ingresa un nivel de confianza: "))
  alpha = 1 - (aceptacion / 100)

  print('------#### PRUEBA DE VARIANZA ####------')
  prueba_varianza(alpha, X)