# marco morquecho NC 1440
import cv2

# Cargar la imagen
imagen = cv2.imread("../imagenes/aveztruz.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 7)

# Mostrar imágenes
cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen con filtro de mediana 1440", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/aveztruz_mediana 1440.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/aveztruz_mediana 1440.jpg")
import os
print("Guardando en:", os.path.abspath("../resultados/aveztruz 1440_mediana.jpg"))

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("marco morquecho NC 1440")