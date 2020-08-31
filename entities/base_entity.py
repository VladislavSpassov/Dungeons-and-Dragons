from abc import ABC, abstractmethod
from helpers_and_utilities.verification_mixin import VerificationMixin


class BaseEntity(ABC, VerificationMixin):
    def __init__(self, health: float = 1, mana: float = 0):
        self.verify_health(health)
        self.health = health
        self.MAX_HEALTH = health

        self.verify_value(mana)
        self.mana = mana
        self.MAX_MANA = mana

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    # TODO IMPLEMENT WHEN CREATE CLASS SPELL
    def can_cast(self):
        pass

    def take_damage(self, damage_points):
        self.verify_value(damage_points)
        self.health -= damage_points

        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        self.verify_value(healing_points)
        self.health += healing_points
        self.health = self.verify_if_more_than_max(
            self.health, self.MAX_HEALTH)

    def take_mana(self, mana_points):
        self.verify_value(mana_points)
        self.mana += mana_points
        self.mana = self.verify_if_more_than_max(self.mana, self.MAX_MANA)

    @abstractmethod
    def attack(self):
        pass
