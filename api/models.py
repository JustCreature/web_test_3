from django.db import models

# Create your models here.

class StatusVals(models.Model):

    value = models.BooleanField("Value", default=False)

    def __str__(self):
        return "UP" if self.value else "DOWN"

    class Meta:
        verbose_name = "Site Status"
        verbose_name_plural = "Site Statuses"
        ordering = ["-value"]

class Site(models.Model):
    name = models.CharField(max_length=200, null=False, default="Unnamed")
    url = models.URLField(null=False, blank=False, default="google.com")
    # status = models.BooleanField(null=False, blank=False, default=False)
    # statuses = models.ForeignKey(StatusVals,
    #                              on_delete=models.CASCADE,
    #                              verbose_name='site_status',
    #                              default=False)

    def __str__(self):
        return self.name




class Pivot(models.Model):
    updated_at = models.DateTimeField("DateTime Updated At", auto_now_add=True)
    status = models.ForeignKey(StatusVals, on_delete=models.CASCADE,
                               verbose_name="status_val")
    site = models.ForeignKey(Site,
                             on_delete=models.CASCADE,
                             verbose_name="site")

    def __str__(self):
        return f"{self.status} - {self.site}"

    class Meta:
        verbose_name = "Pivot Site"
        verbose_name_plural = "Pivot Sites"