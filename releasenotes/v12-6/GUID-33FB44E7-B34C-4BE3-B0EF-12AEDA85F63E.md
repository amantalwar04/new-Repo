---
layout: default
title: Appendix A. RTG4 SPLL and FPLL Calibration and Workaround
nav_order: 10
parent: v12.6
grand_parent: Release Notes
---

# Appendix A. RTG4 SPLL and FPLL Calibration and Workaround

Previously, SPLL \(SERDES PCIe and XAUI\) and FPLL \(FDDR\) lost lock during temperature ramp as described in [CN19009](https://www.microsemi.com/document-portal/doc_download/1244107-cn19009-rtg4-pll-lock-stability)and [CN19009A.](https://www.microsemi.com/document-portal/doc_download/1244685-cn19009a-rtg4-pll-lock-stability-customer-notification-addendum) To resolve this issue, a new CoreABC sequence has been developed in Libero SoC v12.4 that includes an SPLL/FPLL workaround and is available in all later Libero releases. The new sequence requires design changes to the initialization logic \(CoreABC configuration and connections\) in some cases described in the following sections.

