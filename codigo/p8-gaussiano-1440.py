# marco morquecho 1440
import cv2 

# Cargar la imagen subiendo un nivel de carpeta con ".."
imagen = cv2.imread("../imagenes/aveztruz.jpg") 

# Verificar que la imagen se haya cargado 
if imagen is None: 
    print("No se pudo cargar la imagen. Revisa la ruta.") 
    exit() 

# Aplicar filtro Gaussiano 
imagen_suavizada = cv2.GaussianBlur( 
    imagen, 
    (7, 7), 
    0 
) 

# Mostrar imágenes 
cv2.imshow("Imagen original 1440", imagen) 
cv2.imshow("Imagen suavizada 1440 - Filtro Gaussiano", imagen_suavizada) 

# Guardar resultado (también subiendo un nivel si "resultados" está afuera)
cv2.imwrite( 
    "../resultados/aveztruz_gaussiano.jpg", 
    imagen_suavizada 
) 

print("Filtro Gaussiano aplicado correctamente.") 
print("Resultado guardado en:") 
print("../resultados/aveztruz_gaussiano.jpg") 

# Esperar una tecla 
cv2.waitKey(0) 

# Cerrar ventanas 
cv2.destroyAllWindows()
print("programa realizado por marco morquecho 1440")