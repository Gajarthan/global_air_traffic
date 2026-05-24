# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_09:16:18_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-05-24 09:16:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 09:16:18 UTC

- **93,471** saved flights
- **33,064** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,471** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,149,626.5 tonnes** estimated CO2 emissions
- **66,645,012 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3943 |
| 2 | SkyWest Airlines | 3474 |
| 3 | IndiGo | 1940 |
| 4 | EJA | 1771 |
| 5 | American Airlines | 1423 |
| 6 | Southwest Airlines | 1357 |
| 7 | ENY | 1159 |
| 8 | Lufthansa | 1132 |
| 9 | Delta Air Lines | 1026 |
| 10 | Vueling | 888 |
| 11 | LATAM Airlines | 835 |
| 12 | AXM | 821 |
| 13 | WIF | 809 |
| 14 | AZU | 742 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 695 |
| 17 | All Nippon Airways | 694 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 648 |
| 20 | easyJet | 611 |
| 21 | EJU | 598 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 566 |
| 24 | VIV | 555 |
| 25 | Air France | 548 |
| 26 | CXK | 501 |
| 27 | MXY | 495 |
| 28 | Japan Airlines | 487 |
| 29 | AXB | 474 |
| 30 | AIQ | 452 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77375 |
| 2 | 🇪🇸 ES | 6554 |
| 3 | 🇮🇳 IN | 6122 |
| 4 | 🇦🇺 AU | 5735 |
| 5 | 🇩🇪 DE | 5131 |
| 6 | 🇧🇷 BR | 5114 |
| 7 | 🇮🇹 IT | 5073 |
| 8 | 🇨🇦 CA | 4736 |
| 9 | 🇯🇵 JP | 4490 |
| 10 | 🇬🇧 GB | 3980 |
| 11 | 🇫🇷 FR | 3762 |
| 12 | 🇨🇴 CO | 3250 |
| 13 | 🇲🇽 MX | 2877 |
| 14 | 🇬🇷 GR | 2682 |
| 15 | 🇳🇴 NO | 2588 |
| 16 | 🇨🇭 CH | 2438 |
| 17 | 🇲🇾 MY | 2072 |
| 18 | 🇹🇷 TR | 1721 |
| 19 | 🇿🇦 ZA | 1687 |
| 20 | 🇳🇿 NZ | 1594 |
| 21 | 🇹🇭 TH | 1581 |
| 22 | 🇵🇱 PL | 1525 |
| 23 | 🇰🇷 KR | 1492 |
| 24 | 🇵🇭 PH | 1417 |
| 25 | 🇬🇹 GT | 1409 |
| 26 | 🇲🇦 MA | 1071 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 937 |
| 29 | 🇲🇪 ME | 932 |
| 30 | 🇭🇷 HR | 843 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2030 |
| 2 | Denver International Airport |  | US | 1579 |
| 3 | Tokyo International Airport |  | JP | 1497 |
| 4 | Indira Gandhi International Airport |  | IN | 1332 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1241 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1143 |
| 8 | Guaymaral Airport |  | CO | 1133 |
| 9 | Zurich Airport |  | CH | 1086 |
| 10 | La Aurora Airport |  | GT | 1077 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1023 |
| 13 | El Dorado International Airport |  | CO | 1021 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 936 |
| 15 | Chicago O'Hare International Airport |  | US | 893 |
| 16 | Madrid Barajas International Airport |  | ES | 837 |
| 17 | Kuala Lumpur International Airport |  | MY | 818 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 789 |
| 19 | Salt Lake City International Airport |  | US | 787 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 745 |
| 22 | Malpensa International Airport |  | IT | 741 |
| 23 | Bengaluru International Airport |  | IN | 736 |
| 24 | Charles de Gaulle International Airport |  | FR | 729 |
| 25 | Charlotte/Douglas International Airport |  | US | 713 |
| 26 | Congonhas Airport |  | BR | 709 |
| 27 | Daniel K Inouye International Airport |  | US | 673 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 629 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 625 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 610 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 594 |
| 35 | Vitoria/Foronda Airport |  | ES | 584 |
| 36 | Don Mueang International Airport |  | TH | 580 |
| 37 | Amsterdam Airport Schiphol |  | NL | 577 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 534 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 465 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 239 | 1h 26m | 910 km | 3,750.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 235 | 28m | 304 km | 1,231.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 214 | 1h 10m | 770 km | 2,842.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 135 | 14m | 154 km | 357.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 115 | 1h 40m | 1,156 km | 2,294.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA064 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-23 22:03 UTC | 2026-05-24 09:16 UTC | 11h 12m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-05-24 08:00 UTC | 2026-05-24 09:09 UTC | 1h 9m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-05-24 08:45 UTC | 2026-05-24 08:51 UTC | 6m |
| GBGGO | GBG | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-24 08:23 UTC | 2026-05-24 08:49 UTC | 26m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-05-24 08:43 UTC | 2026-05-24 08:48 UTC | 5m |
| N129RR |  | Phoenix Deer Valley Airport (KDVT) | Western Sky Airpark (0AZ2) | 2026-05-24 07:43 UTC | 2026-05-24 08:43 UTC | 1h 0m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-05-24 08:26 UTC | 2026-05-24 08:38 UTC | 12m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-05-24 06:46 UTC | 2026-05-24 08:37 UTC | 1h 50m |
| IHFRT | IHF | Milano / Bresso Airport (LIMB) | Milano / Bresso Airport (LIMB) | 2026-05-24 08:34 UTC | 2026-05-24 08:35 UTC | 1m |
| DHFCB | DHF | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-05-24 08:29 UTC | 2026-05-24 08:34 UTC | 5m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | MoD Boscombe Down Airport (EGDM) | 2026-05-24 07:49 UTC | 2026-05-24 08:29 UTC | 40m |
| DHK362 | DHK | Leipzig Halle Airport (EDDP) | John F Kennedy International Airport (KJFK) | 2026-05-24 00:18 UTC | 2026-05-24 08:28 UTC | 8h 9m |
| VLG63LZ | Vueling | Barcelona International Airport (LEBL) | Garray Airport (LEGY) | 2026-05-24 07:51 UTC | 2026-05-24 08:27 UTC | 36m |
| HBZYR | HBZ | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-05-24 08:18 UTC | 2026-05-24 08:27 UTC | 9m |
| N741AC |  | Iowa City Municipal Airport (KIOW) | Iowa City Municipal Airport (KIOW) | 2026-05-24 08:24 UTC | 2026-05-24 08:26 UTC | 2m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-05-24 08:14 UTC | 2026-05-24 08:26 UTC | 12m |
| KQA305 | KQA | Jomo Kenyatta International Airport (HKJK) | Jomo Kenyatta International Airport (HKJK) | 2026-05-24 08:24 UTC | 2026-05-24 08:24 UTC | 0m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-24 07:48 UTC | 2026-05-24 08:19 UTC | 31m |
| TITAN122 | TIT | Jomo Kenyatta International Airport (HKJK) | Jomo Kenyatta International Airport (HKJK) | 2026-05-24 08:18 UTC | 2026-05-24 08:18 UTC | 0m |
| ZKHUP | ZKH | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-05-24 08:08 UTC | 2026-05-24 08:17 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
