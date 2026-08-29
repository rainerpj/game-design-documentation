from pathlib import Path
import argparse
from datetime import date


CHAPTERS = [
    (1, "PROJECT_OVERVIEW", "项目概览", "Project Overview"),
    (2, "PLAYER_EXPERIENCE", "玩家体验总览", "Player Experience"),
    (3, "WORLD_NARRATIVE_ATMOSPHERE", "世界观、叙事与氛围", "World, Narrative, and Atmosphere"),
    (4, "CONTROLS_CAMERA_CHARACTER_STATE", "操控、镜头与角色状态", "Controls, Camera, and Character State"),
    (5, "COMBAT_SYSTEM", "战斗系统", "Combat System"),
    (6, "ENEMIES_AI_ENCOUNTERS", "敌人、AI 与遭遇", "Enemies, AI, and Encounters"),
    (7, "ITEMS_INVENTORY_ECONOMY", "物品、背包与资源经济", "Items, Inventory, and Economy"),
    (8, "SHOPS_RUN_BUILDS", "商店与局内构筑", "Shops and Run Builds"),
    (9, "META_PROGRESSION_SAVE_RESULTS", "局外成长、存档与结算", "Meta Progression, Saves, and Results"),
    (10, "WORLD_MAP_LEVELS", "世界、地图与关卡", "World, Maps, and Levels"),
    (11, "QUESTS_EVENTS_FLOW", "任务、事件与流程", "Quests, Events, and Flow"),
    (12, "UI_UX_INFORMATION", "UI、UX 与信息架构", "UI, UX, and Information"),
    (13, "ART_ANIMATION_VFX_AUDIO", "美术、动画、特效与音频", "Art, Animation, VFX, and Audio"),
    (14, "TECHNICAL_DATA_ARCHITECTURE", "技术设计与数据架构", "Technical and Data Architecture"),
    (15, "SCOPE_VERSION_PLAN", "内容范围与版本规划", "Scope and Version Plan"),
    (16, "PRODUCTION_COLLABORATION", "制作计划与团队协作", "Production and Collaboration"),
    (17, "TEST_BALANCE_QUALITY", "测试、平衡与质量标准", "Test, Balance, and Quality"),
    (18, "RELEASE_OPERATIONS_COMPLIANCE", "发行、运营与合规", "Release, Operations, and Compliance"),
    (19, "RISKS_ASSUMPTIONS_OPEN_QUESTIONS", "风险、假设与开放问题", "Risks, Assumptions, and Open Questions"),
    (20, "APPENDICES_TABLES", "附录与配套表格", "Appendices and Tables"),
]

PROFILE_CHAPTERS = {
    "concept": {1, 2, 15, 19},
    "prototype": {1, 2, 15, 17, 19},
    "vertical-slice": {1, 2, 12, 13, 14, 15, 16, 17, 19},
    "production": set(range(1, 21)),
}

STARTERS = {
    "zh": {
        1: ["产品定位", "目标玩家", "体验支柱", "差异化", "平台与模式", "成功标准"],
        2: ["玩家幻想", "核心循环", "单局与长期循环", "决策节奏", "失败与恢复"],
        15: ["原型范围", "垂直切片", "MVP 包含", "MVP 明确不包含", "版本退出标准"],
        19: ["风险台账", "核心假设验证", "开放问题", "负责人、截止点与回退方案"],
        "default": ["目标与玩家价值", "当前结论", "规则与流程", "依赖与边界", "MVP 范围", "验收标准", "开放问题"],
    },
    "en": {
        1: ["Positioning", "Target Players", "Experience Pillars", "Differentiation", "Platforms and Modes", "Success Criteria"],
        2: ["Player Fantasy", "Core Loop", "Session and Long-Term Loops", "Decision Rhythm", "Failure and Recovery"],
        15: ["Prototype Scope", "Vertical Slice", "MVP Inclusions", "MVP Exclusions", "Version Exit Criteria"],
        19: ["Risk Register", "Core Assumption Tests", "Open Questions", "Owners, Decision Points, and Fallbacks"],
        "default": ["Goal and Player Value", "Current Decision", "Rules and Flow", "Dependencies and Boundaries", "MVP Scope", "Acceptance Criteria", "Open Questions"],
    },
}


def write_new(path: Path, text: str):
    if path.exists():
        return False
    path.write_text(text, encoding="utf-8")
    return True


def parse_extra_chapters(raw: str):
    if not raw:
        return set()
    values = set()
    for token in raw.split(","):
        try:
            value = int(token.strip())
        except ValueError as exc:
            raise argparse.ArgumentTypeError(f"Invalid chapter number: {token}") from exc
        if value < 1 or value > 20:
            raise argparse.ArgumentTypeError(f"Chapter number must be 1-20: {value}")
        values.add(value)
    return values


def companion_text(language: str, kind: str, title: str):
    if language == "zh":
        if kind == "decision":
            return f"# {title} 决策记录\n\n| ID | 日期 | 状态 | 决策 | 理由 | 影响范围 | 批准人 |\n|---|---|---|---|---|---|---|\n"
        return (
            f"# {title} 实验记录\n\n"
            "研究材料、实验结果和正式规则应保持分离。实验被采纳后，更新权威章节并记录影响范围。\n\n"
            "| ID | 状态 | 假设 | 原型版本/入口 | 判定指标 | 结果 | 权威更新 |\n"
            "|---|---|---|---|---|---|---|\n"
        )
    if kind == "decision":
        return f"# {title} Decision Log\n\n| ID | Date | Status | Decision | Rationale | Impact | Approver |\n|---|---|---|---|---|---|---|\n"
    return (
        f"# {title} Experiment Log\n\n"
        "Keep research, experiment evidence, and authoritative rules separate. Update the authority and impact map after adoption.\n\n"
        "| ID | Status | Hypothesis | Prototype Version/Entry | Measures | Result | Authority Update |\n"
        "|---|---|---|---|---|---|---|\n"
    )


def main():
    ap = argparse.ArgumentParser(description="Create a non-destructive, profile-based GDD skeleton.")
    ap.add_argument("project_root")
    ap.add_argument("--title", required=True)
    ap.add_argument("--language", choices=["zh", "en"], default="zh")
    ap.add_argument("--profile", choices=list(PROFILE_CHAPTERS), default="concept")
    ap.add_argument("--chapters", default="", help="Additional chapter numbers, comma separated (for example 4,5,6).")
    args = ap.parse_args()

    root = Path(args.project_root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    selected = PROFILE_CHAPTERS[args.profile] | parse_extra_chapters(args.chapters)
    created = []

    if args.language == "zh":
        index_title = f"# {args.title} 项目策划案索引"
        index_meta = [f"> 建立日期：{date.today().isoformat()}", f"> 文档档位：{args.profile}", "> Canonical status: [Proposal]", "> 显示状态：[提案]"]
        body_heading = "## 正文"
        supporting_heading = "## 配套资料"
        companion_links = ["- [决策记录](./DECISION_LOG.md)"]
    else:
        index_title = f"# {args.title} Game Design Document Index"
        index_meta = [f"> Created: {date.today().isoformat()}", f"> Profile: {args.profile}", "> Status: [Proposal]"]
        body_heading = "## Chapters"
        supporting_heading = "## Supporting Records"
        companion_links = ["- [Decision log](./DECISION_LOG.md)"]

    index_lines = [index_title, "", *index_meta, "", body_heading, ""]
    for number, slug, zh_title, en_title in CHAPTERS:
        if number not in selected:
            continue
        chapter_title = zh_title if args.language == "zh" else en_title
        filename = f"CHAPTER_{number:02d}_{slug}.md"
        index_lines.append(f"{number}. [{chapter_title}](./{filename})")
        sections = STARTERS[args.language].get(number, STARTERS[args.language]["default"])
        if args.language == "zh":
            body = [f"# 第{number}章：{chapter_title}", "", "> Canonical status: [Proposal]", "> 显示状态：[提案]", f"> 项目：{args.title}", ""]
            placeholder = "[待补充]"
        else:
            body = [f"# Chapter {number}: {chapter_title}", "", "> Status: [Proposal]", f"> Project: {args.title}", ""]
            placeholder = "[To be completed]"
        for section_number, section in enumerate(sections, 1):
            body.extend([f"## {number}.{section_number} {section}", "", placeholder, ""])
        if write_new(root / filename, "\n".join(body).rstrip() + "\n"):
            created.append(filename)

    if write_new(root / "DECISION_LOG.md", companion_text(args.language, "decision", args.title)):
        created.append("DECISION_LOG.md")

    if args.profile in {"prototype", "vertical-slice", "production"}:
        if write_new(root / "EXPERIMENT_LOG.md", companion_text(args.language, "experiment", args.title)):
            created.append("EXPERIMENT_LOG.md")
        companion_links.append("- [实验记录](./EXPERIMENT_LOG.md)" if args.language == "zh" else "- [Experiment log](./EXPERIMENT_LOG.md)")

    index_lines.extend(["", supporting_heading, "", *companion_links, ""])
    if args.language == "zh":
        index_lines.extend(["- 系统规格与 Feature Contract", "- 配置表与字段字典", "- 风险、测试与变更记录", ""])
    else:
        index_lines.extend(["- System specifications and Feature Contracts", "- Configuration tables and field dictionary", "- Risk, test, and change records", ""])

    if write_new(root / "PROJECT_DESIGN_DOCUMENT_INDEX.md", "\n".join(index_lines)):
        created.append("PROJECT_DESIGN_DOCUMENT_INDEX.md")

    print(f"Created {len(created)} files in {root}")
    print(f"Profile={args.profile}; chapters={','.join(str(n) for n in sorted(selected))}")
    existing_selected = [
        f"CHAPTER_{number:02d}_{slug}.md"
        for number, slug, _, _ in CHAPTERS
        if number in selected and (root / f"CHAPTER_{number:02d}_{slug}.md").exists()
    ]
    if any(filename not in created for filename in existing_selected):
        print("Existing files were preserved and not overwritten.")


if __name__ == "__main__":
    main()
