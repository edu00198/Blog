from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="contenido",
            field=models.TextField(max_length=2000),
        ),
    ]
