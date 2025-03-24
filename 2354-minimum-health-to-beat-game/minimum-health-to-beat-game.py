class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total_damage = 0
        max_damage = damage[0]
        for d in damage:
            total_damage += d
            max_damage = max(max_damage, d)
        
        return total_damage - min(max_damage, armor) + 1