from django.test import TestCase
from django.urls import reverse

from .models import MAX_COMENTARIO_LENGTH, Comentario, Post


class ComentarioLengthTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(titulo="Post de prueba", contenido="Contenido")
        self.url = reverse("detalle_post", args=[self.post.id])

    def test_accepts_comment_at_maximum_length(self):
        response = self.client.post(self.url, {
            "nombre": "Ana",
            "contenido": "a" * MAX_COMENTARIO_LENGTH,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comentario.objects.count(), 1)

    def test_rejects_comment_over_maximum_length(self):
        response = self.client.post(self.url, {
            "nombre": "Ana",
            "contenido": "a" * (MAX_COMENTARIO_LENGTH + 1),
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comentario.objects.count(), 0)
        self.assertContains(response, "no puede superar los 2000 caracteres")

    def test_comment_textarea_exposes_maximum_length(self):
        response = self.client.get(self.url)

        self.assertContains(response, 'maxlength="2000"')
