from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from apps.core import choices


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Session(Timestamp):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    description = models.CharField(
        verbose_name=_("Descrição"), 
        max_length=20, 
        null=True, 
        blank=True
    )
    status = models.CharField(
        verbose_name=_("Status"), 
        max_length=30, 
        choices=choices.SESSION_STATUS, 
        default=choices.WAITING_PARTICIPANTS
    )
    allow_observers = models.BooleanField(
        verbose_name=_("Permitir observadores?"), 
        default=True
    )
    allow_participants_reset_votes = models.BooleanField(
        verbose_name=_("Participantes têm permissão para redefinir votos"), 
        default=False
    )

    class Meta:
        verbose_name=_("Sessão")
        verbose_name_plural=_("Sessões")

    def __str__(self):
        return f"{self.id}"


class SessionUser(Timestamp):
    name = models.CharField(
        verbose_name=_("Nome"), 
        max_length=20
    )
    session = models.ForeignKey(
        Session, 
        verbose_name=_("Sessão"), 
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name=_("Função"),
        max_length=30,
        choices=choices.USER_ROLE,
        default=choices.OBSERVER
    )

    class Meta:
        verbose_name = _("Usuário da Sessão")
        verbose_name_plural = _("Usuários da Sessão")

    def __str__(self):
        return f"#{self.id}/{self.get_role_display()} - {self.name}"


class PointingPoker(Timestamp):
    description = models.CharField(
        verbose_name=_("Descrição"), 
        max_length=20, 
        null=True, 
        blank=True
    )
    session = models.ForeignKey(
        Session, 
        verbose_name=_("Sessão"), 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = verbose_name_plural = _("Pointing Poker")

    def __str__(self):
        return self.description


class PointValue(Timestamp):
    pointing_poker = models.ForeignKey(
        PointingPoker, 
        verbose_name=_("Pointing Poker"), 
        on_delete=models.CASCADE
    )
    label = models.CharField(
        verbose_name=_("Descrição"), 
        max_length=10
    )
    value = models.PositiveIntegerField(verbose_name=_("Valor"))    

    class Meta:
        verbose_name=verbose_name_plural=_("Valores de pontos")
        ordering=["value"]

    def __str__(self):
        return f"{self.label}/{self.value}"


class Estimate(Timestamp):
    session = models.ForeignKey(
        Session, 
        verbose_name=_("Sessão"), 
        on_delete=models.CASCADE
    )
    is_closed = models.BooleanField(
        verbose_name=_("Finalizado"),
        default=False
    )
    score = models.DecimalField(
        verbose_name=_("Pontuação"), 
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    start_at = models.DateTimeField(
        verbose_name=_("Dt. Início"),
        auto_now_add=True,
        null=True,
        blank=True
    )
    close_at = models.DateTimeField(
        verbose_name=_("Dt. Fim"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name=_("Estimativa")
        verbose_name_plural=_("Estimativas")


    def __str__(self):
        return f"#{self.id} Estimativa: {self.session}"


class UserEstimate(Timestamp):
    estimate = models.ForeignKey(
        Estimate, 
        verbose_name=_("Estimativa"), 
        on_delete=models.CASCADE
    )    
    point_value = models.ForeignKey(
        PointValue, 
        verbose_name=_("Pontuação"), 
        on_delete=models.CASCADE
    )
    session_user = models.ForeignKey(
        SessionUser, 
        verbose_name=_("Usuário"), 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name=_("Estimativa do usuário")
        verbose_name_plural=_("Estimativas dos usuários")


    def __str__(self):
        return f"{self.estimate} - {self.point_value} - {self.session_user}"