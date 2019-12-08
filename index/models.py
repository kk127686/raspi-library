from django.db import models


# Create your models here.


class Product(models.Model):
    pro_name = models.CharField(verbose_name='物品名称', max_length=30)
    pro_num = models.IntegerField(verbose_name='物品数量')
    pro_cate = models.ForeignKey("ProductCate", on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name_plural = "物品管理"
        managed = True
        db_table = 'product'


class ProductCate(models.Model):
    cate_name = models.CharField(verbose_name='物品分类', max_length=10)
    # cate_remarks = models.CharField(verbose_name="备注", max_length=50)
    cate_date = models.DateField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_cate'
