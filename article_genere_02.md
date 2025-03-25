 # Analyse de l'image avec OpenCV et Python

L'analyse d'images est un domaine important de la programmation. Dans ce guide, nous allons apprendre à utiliser OpenCV, une bibliothèque populaire pour traiter les images en temps réel, dans des applications Python.

## Prérequis

Avant de commencer, il est nécessaire d'installer OpenCV et Python sur votre système. Vous pouvez trouver les instructions de téléchargement et d'installation sur le [site Web d'OpenCV](https://opencv.org/).

## Créer un nouveau fichier Python

Ouvrez un éditeur de texte ou IDE favori, et créez un nouveau fichier Python. Nous allons appeler ce fichier `image_analysis.py`.

## Chargement de l'image

Pour charger une image avec OpenCV, utilisez la fonction `imread()`:

```python
import cv2

img = cv2.imread('mon_image.jpg')
```

Assurez-vous que l'image se trouve dans le même dossier que votre fichier Python.

## Afficher l'image chargée

Pour afficher l'image chargée, utilisez la fonction `imshow()`:

```python
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

La fenêtre de l'image s'ouvrira automatiquement lorsque vous exécuterez votre code. Les flèches du clavier permettent de naviguer entre les différentes images ouvertes.

## Effectuer des opérations sur l'image

OpenCV dispose d'une grande variété d'opérations pour traiter les images. Voici quelques-unes des fonctionnalités les plus courantes :

### Conversion en gris

Pour convertir une image couleur en gris, utilisez la fonction `cvtColor()`:

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Appliquer un filtre

Pour appliquer un filtre à une image, utilisez la fonction `filter2D()`:

```python
blur = cv2.GaussianBlur(img, (5, 5), 0)
```

### Extraire des contours

Pour extraire les contours d'une image, utilisez la fonction `findContours()`:

```python
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

## Enregistrement d'une image traitée

Pour enregistrer une image traitée, utilisez la fonction `imwrite()`:

```python
cv2.imwrite('image_traitée.jpg', resultat)
```

## Conclusion

Nous avons appris à charger des images avec OpenCV et à les traiter en utilisant quelques-unes de ses fonctionnalités les plus courantes. Vous pouvez maintenant explorer d'autres fonctionnalités pour améliorer vos propres applications d'analyse d'images.

Au cas où vous rencontreriez des problèmes, n'hésitez pas à consulter la [documentation officielle d'OpenCV](https://docs.opencv.org/master/) ou à poser une question sur le forum OpenCV.