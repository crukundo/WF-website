# Generated by Django 2.1.7 on 2019-05-18 21:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_auto_20190518_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('card', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], help_text='Whether to align the image left or right on the block.', required=False)), ('extra', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=False)), ('page_link', wagtail.core.blocks.PageChooserBlock(requried=False))]))], block_counts={'button': 1}))]))], null=True),
        ),
    ]