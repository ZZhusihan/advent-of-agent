.PHONY: help day1 day2 day3 day4 day5 day6 day7 day8 day9 day10 day11 day12 day13 day14 day15 day16 day17 day18 day19 day20 day21 day22 day23 day24 day25

help:
	@echo "Advent of Agents - Day Notes Generator"
	@echo ""
	@echo "Usage:"
	@echo "  make day<N>     - Create notes file for day N (e.g., make day2)"
	@echo "  make help       - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make day3       - Creates notes/day-03.md"
	@echo "  make day25      - Creates notes/day-25.md"

day1 day2 day3 day4 day5 day6 day7 day8 day9 day10 day11 day12 day13 day14 day15 day16 day17 day18 day19 day20 day21 day22 day23 day24 day25:
	@DAY_NUM=$$(echo $@ | sed 's/day//'); \
	python3 make-day.py $$DAY_NUM
