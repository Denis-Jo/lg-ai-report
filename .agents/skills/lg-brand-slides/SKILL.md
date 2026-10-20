---
name: lg-brand-slides
description: 발표용 Single Webpage 제작 시 LG 브랜드 시그니처 색상(Hex)과 미니멀 레이아웃을 고정하는 스킬
---

# LG Brand Presentation Webpage Skill

## 1. 고정 색상 팔레트 (Hex Code Strict Enforcement)
프레젠테이션 웹페이지(`index.html`)를 생성하거나 수정할 때 반드시 아래 Hex 색상 코드만 사용하며, 임의의 파란색/보라색 그라데이션 사용을 금지합니다.
- **Primary Brand Accent**: `#A50034` (LG Heritage Red — 상단 배지, 카드 상단 포인트 보더, 핵심 강조 수치에만 제한적 사용)
- **Main Background**: `#FFFFFF` (Pure White — 눈이 편한 깔끔한 흰색 배경)
- **Card / Section Surface**: `#F8F9FA` (Soft Gray — 본문 카드 배경 및 코드 영역)
- **Border / Divider**: `#E5E7EB` (1px 실선 구분선)
- **Typography**: 제목 `#111827` (Charcoal Black), 본문 `#374151` (Slate Gray), 캡션 `#6B7280`

## 2. 인터랙션 및 구조 규칙
1. 외부 프레임워크 없이 **단일 HTML 파일(`Single Page HTML`)** 안에 인라인 CSS와 Vanilla JS를 포함하여 어디서든 더블클릭으로 열리게 작성합니다.
2. 키보드 좌우 방향키(`ArrowLeft`, `ArrowRight`) 및 하단 페이지 인디케이터(`1 / N`)를 기본 탑재합니다.
