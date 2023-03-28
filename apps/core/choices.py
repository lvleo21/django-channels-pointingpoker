from django.utils.translation import gettext_lazy as _


WAITING_PARTICIPANTS="waiting_participants"
IN_PROGRESS="in_progress"
CLOSED="closed"
SESSION_STATUS=(
    (WAITING_PARTICIPANTS, _("Aguardando participantes")),
    (IN_PROGRESS, _("Em andamento")),
    (CLOSED, _("Finalizado"))
)

OBSERVER="observer"
OWNER="owner"
PLAYER="player"
USER_ROLE=(
    (OBSERVER, _("Observador(a)")),
    (OWNER, _("Dono(a)")),
    (PLAYER, _("Jogador(a)")),
)