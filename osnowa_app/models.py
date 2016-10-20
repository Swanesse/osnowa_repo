# encoding: utf-8

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Point(models.Model):
    autor = models.ForeignKey('auth.User')
    arkusz_mapy = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200, verbose_name='Nazwa')
    klasa = models.CharField(max_length=200)
    numer_katalogowy = models.CharField(max_length=200)
    wojewodztwo = models.CharField(max_length=200)
    powiat = models.CharField(max_length=200)
    gmina = models.CharField(max_length=200)
    miejscowosc = models.CharField(max_length=200)
    wsp_2000 = models.CharField(max_length=200, default='')
    wsp_lokalne = models.CharField(max_length=200, default='')
    wsp_WGS84 = models.CharField(max_length=200, default='')
    stabilizacja = models.CharField(max_length=200, default='')
    typ_znaku = models.CharField(max_length=200, default='')
    zdjecie = models.ImageField(upload_to='static/images/', default="static/images/znak.jpg")
    created_date = models.DateTimeField(default=timezone.now)
    find_date = models.DateTimeField(blank=True, null=True)
    odnaleziony = models.IntegerField(default=0)
    uszkodzony = models.IntegerField(default=0)

    def publish(self):
        self.find_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa



class LatLng(models.Model):
    """
    Klasa odpowiada punktowi `GLatLng` na mapie `Google Maps`. Atrybuty:
        * :mod:`latit` -- wskazuje szerokość geograficzną
        * :mod:`longi` -- wskazuje długość geograficzną
    """
    latit = models.FloatField()
    longi = models.FloatField()

class Point2(LatLng):
    """
    Każdy użytkownik może umieścić na mapie opisywalny punkt. Dziedziczy po klasie LatLng.
    Opis punktu jest ciągiem znaków nie dłuższym niż 120. Atrybuty:
        * :mod:`user` -- wskazuje obiekt użytkownika
        * :mod:`desc` -- opis punktu
    """
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=120)

    def __unicode__(self):
        return "%s created point (%s,%s)" % (self.user, self.latit, self.longi)


class Map(models.Model):
    """
    Każda mapa posiada nazwę, przyjazny adres utworzony na podstawie nazwy,
    słowa kluczowe, miasto, ciąg punktów z których złożona jest ścieżka,
    długość trasy w kilometrach oraz współrzędne krańcowe mapy.
    Nazwa mapy jest ciągiem znaków nieprzekraczającym 256.
    Przyjazny adres (ang. `slug`) to ciąg znaków nieprzekraczający 50.
    Słowa kluczowe
    """
    name = models.CharField(max_length=256, verbose_name='Nazwa')
    slug = models.SlugField()
    tags = models.CharField(max_length=512, verbose_name='Tagi')
    city = models.CharField(max_length=32, verbose_name='Miasto')
    latlngs = models.TextField(verbose_name='Współrzędne')
    distance = models.FloatField(verbose_name='Dystans')
    southwest = models.ForeignKey(LatLng, related_name="%(class)s_sw")
    northeast = models.ForeignKey(LatLng, related_name="%(class)s_ne")

    def getlatlngs(self):
        """
        Zwraca tablicę par (lat, lng). Atrybut :mod:`latlngs` zawiera ciąg
        znaków odpowiadających kolejnym punktom na trasie.::
            10.0,20.3;20.4,50.4;
        Powyższy ciąg zostanie zmieniony w tablicę par.
            >>> map = Map(latlngs='10.0,20.3;20.4,50.4;')
            >>> map.getlatlngs()
            [(10.0, 20.300000000000001), (20.399999999999999, 50.399999999999999)]
        """
        result = []
        for p in self.latlngs.split(';'):
            if p:
                lat, lng = p.split(',')
                pair = float(lat), float(lng)
                result.append(pair)
        return result

    # def jsonlatlngs(self):
    #     """
    #     Zwraca napis reprezentujący atrybut :mod:`latlngs` w formacie JSON.
    #     """
    # result = "["
    #     for p in self.latlngs.split(';'):
    #         if p:
    #             result += '['+p+'],'
    #     return result[:-1] + ']'
    #
    # def getcenter(self):
    # """
    #     Zwraca środek mapy w oparciu o współrzędne krańcowe trasy.
    #     """
    # horizontal = (self.northeast.latit + self.southwest.latit) / 2
    # vertical   = (self.northeast.longi + self.southwest.longi) / 2
    # return [horizontal, vertical]
    #
    # def gettags(self):
    #     """
    #     Każde słowo kluczowe jest ciągiem znaków. Atrybut :mod:`tags` zawiera
    #     słowa kluczowe oddzielone pojedynczym odstępem.
    #     Metoda zwraca tablicę słów kluczowych.
    #         >>> map = Map(tags=u'abc, grunwaldzka, rondo regana')
    #         >>> map.gettags()
    #         [u'abc', u'grunwaldzka', u'rondo regana']
    #     """
    #     return [ tag.strip() for tag in self.tags.split(',') ]
    #
    # def save(self):
    #     """
    #     Zapisuje mapę do bazy danych tworząc przyjazną nazwę mapy (ang. slug)
    #     używaną przy tworzeniu adresów map. Zamienia słowa kluczowe na wersję
    #     bez polskich znaków, spacji oraz znaków interpunkcyjnych.
    #     """
    #     self.slug = slugify(self.name)
    #     self.tags = ','.join([ slugify(tag.strip()) for tag in self.tags.split(',') ])
    #     super(Map, self).save()
    #
    # def __unicode__(self):
    #     return self.name
    #
    # __str__ = __unicode__
