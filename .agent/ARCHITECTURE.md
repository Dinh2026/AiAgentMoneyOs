# AI Agent Money OS — Architecture

> Hệ thống AI Agent thực chiến — Software delivery + Business growth automation.
>
> Phát triển bởi **Vương Duy Định**.

## Overview

AI Agent Money OS kết hợp engineering execution với money-focused business operating layer, giúp solopreneur xây dựng và vận hành business tự động từ A-Z.

| Component | Count | Path |
| --- | ---: | --- |
| Agents | 25 | `.agent/agents/` |
| Skills | 67 | `.agent/skills/` |
| Workflows | 16 | `.agent/workflows/` |
| Commands | 18 | `.agent/commands/` |
| Claude Commands | 18 | `.agent/.claude/commands/` |
| Shared Data | 1 package | `.agent/.shared/` |
| Runtime Scripts | 5 scripts | `.agent/scripts/` |

## Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          ← This file
├── AI_AGENT_MONEY_OS_BUSINESS_LAYER.md
├── README.md                ← Main documentation
├── SKILLS_INDEX_VI.md       ← Skills index with Vietnamese names
├── agents/                  ← 25 specialist agents
├── commands/                ← 18 slash commands
├── .claude/commands/        ← Claude-specific commands
├── rules/                   ← GEMINI.md + behavior rules
├── scripts/                 ← Runtime scripts
├── skills/                  ← 67 skills (Marketing + Business + Engineering)
├── workflows/               ← 16 workflows
├── .shared/                 ← Shared resources
└── mcp_config.json          ← MCP server configuration
```

## Agent Layers

### Engineering Agents (20)

Core software specialists: coding, architecture, UI, API, database, testing, security, DevOps, mobile, game, SEO, product, documentation, debugging, performance.

### Money OS Business Agents (5)

| Agent | Focus | Key Skills |
| --- | --- | --- |
| `01-offer-agent` | Market research, competitor analysis, offer design | `market-research`, `competitor-analysis`, `offer-packaging` |
| `02-attraction-agent` | Funnels, content, lead magnets | `funnel-architecture`, `content-creation`, `lead-magnet-builder` |
| `03-conversion-agent` | Sales pages, copy, objections | `sales-page-blueprint`, `copywriting`, `objection-handler` |
| `04-deliver-agent` | Payments, delivery, notifications, landing pages | `payment-setup-guide`, `notification-setup-guide`, `delivery-setup-guide`, `landing-page-builder`, `vercel-deployment`, `payment-embed` |
| `05-insights-agent` | Analytics, revenue, optimization | `social-analytics`, `revenue-report`, `optimization-advisor` |

## Marketing Skills — 12 Kỹ Năng Bán Hàng

Pipeline marketing hoàn chỉnh theo framework Hormozi + Sabri Suby:

| # | Skill | Tên Tiếng Việt | Focus |
|---|-------|----------------|-------|
| 01 | `avatar-builder` | Xây Dựng Chân Dung Khách Hàng | Dream Buyer Avatar |
| 02 | `brand-voice` | Xây Dựng Giọng Nói Thương Hiệu | Voice Profile |
| 03 | `hero-mechanism` | Xây Dựng USP | Proprietary method |
| 04 | `money-model` | Thiết Kế Money Model | Revenue model |
| 05 | `offer-architect` | Xây Dựng Offer Không Thể Chối Từ | Offer packaging |
| 06 | `hvco-creator` | Tạo Nội Dung Giá Trị Cao | Lead magnet brief |
| 07 | `funnel-strategist` | Thiết Kế Blueprint Phễu Bán Hàng | Customer journey |
| 08 | `ad-copy-machine` | Máy Viết Copy Quảng Cáo | Funnel copy |
| 09 | `vsl-scriptwriter` | Viết Kịch Bản Video Bán Hàng | VSL scripts |
| 10 | `email-closer` | Viết Email Bán Hàng Tự Động | Email sequences |
| 11 | `follow-up-engine` | Hệ Thống Follow-up | Re-engagement |
| 12 | `sales-call-script` | Kịch Bản Gọi Điện Bán Hàng | Sales call scripts |

## Business Commands

| Command | Agent |
| --- | --- |
| `/research`, `/competitor`, `/offer` | `01-offer-agent` |
| `/funnel`, `/content`, `/lead-magnet` | `02-attraction-agent` |
| `/sales-page`, `/copy`, `/objection` | `03-conversion-agent` |
| `/payment-setup`, `/notification`, `/delivery`, `/landing-page`, `/deploy`, `/payment-embed` | `04-deliver-agent` |
| `/analytics`, `/revenue`, `/optimize` | `05-insights-agent` |

## Business Workflows

| Workflow | Output |
| --- | --- |
| `offer-research-workflow.md` | Validated niche and packaged offer |
| `attraction-content-workflow.md` | Funnel and content system |
| `conversion-sales-workflow.md` | Sales assets and conversion flow |
| `delivery-automation-workflow.md` | Payment, notification, and delivery setup |
| `insights-reporting-workflow.md` | Weekly analytics and optimization report |

## Skill Loading Protocol

```plaintext
User request
  -> classify intent
  -> select agent
  -> read agent frontmatter
  -> load required SKILL.md files
  -> read only relevant references/templates/scripts
  -> execute workflow or command
  -> deliver output
```

## Installable Unit

The `.agent` folder is the installable runtime. To upgrade another project, copy this `.agent` folder into that project root.

---

*AI Agent Money OS © Vương Duy Định*
