# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_15:40:31_UTC-green)

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

**Latest saved flight:** 2026-05-08 15:40:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 15:40:31 UTC

- **73,415** saved flights
- **27,199** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **73,415** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **903,895.2 tonnes** estimated CO2 emissions
- **52,399,722 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3156 |
| 2 | SkyWest Airlines | 2716 |
| 3 | IndiGo | 1659 |
| 4 | EJA | 1342 |
| 5 | American Airlines | 1141 |
| 6 | Southwest Airlines | 1060 |
| 7 | Lufthansa | 956 |
| 8 | ENY | 916 |
| 9 | Vueling | 715 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 681 |
| 12 | WIF | 638 |
| 13 | Delta Air Lines | 633 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 590 |
| 16 | QLK | 573 |
| 17 | Swiss International | 563 |
| 18 | LXJ | 538 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 485 |
| 21 | EJU | 474 |
| 22 | AEE | 470 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 426 |
| 27 | AXB | 410 |
| 28 | CXK | 372 |
| 29 | AIQ | 366 |
| 30 | MXY | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58705 |
| 2 | 🇪🇸 ES | 5314 |
| 3 | 🇮🇳 IN | 5213 |
| 4 | 🇦🇺 AU | 4905 |
| 5 | 🇩🇪 DE | 4119 |
| 6 | 🇧🇷 BR | 4111 |
| 7 | 🇮🇹 IT | 4022 |
| 8 | 🇯🇵 JP | 3876 |
| 9 | 🇨🇦 CA | 3659 |
| 10 | 🇬🇧 GB | 3164 |
| 11 | 🇫🇷 FR | 2912 |
| 12 | 🇨🇴 CO | 2684 |
| 13 | 🇲🇽 MX | 2283 |
| 14 | 🇬🇷 GR | 2176 |
| 15 | 🇳🇴 NO | 2049 |
| 16 | 🇨🇭 CH | 2005 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1437 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1319 |
| 21 | 🇹🇭 TH | 1314 |
| 22 | 🇵🇱 PL | 1229 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1153 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 873 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 787 |
| 29 | 🇳🇱 NL | 769 |
| 30 | 🇧🇸 BS | 615 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1622 |
| 2 | Tokyo International Airport |  | JP | 1302 |
| 3 | Denver International Airport |  | US | 1221 |
| 4 | Indira Gandhi International Airport |  | IN | 1099 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1066 |
| 6 | Frankfurt am Main International Airport |  | DE | 951 |
| 7 | Harry Reid International Airport |  | US | 911 |
| 8 | Guaymaral Airport |  | CO | 879 |
| 9 | El Dorado International Airport |  | CO | 878 |
| 10 | Zurich Airport |  | CH | 868 |
| 11 | La Aurora Airport |  | GT | 859 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 734 |
| 14 | Chicago O'Hare International Airport |  | US | 707 |
| 15 | Kuala Lumpur International Airport |  | MY | 696 |
| 16 | Madrid Barajas International Airport |  | ES | 688 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 648 |
| 18 | Malpensa International Airport |  | IT | 639 |
| 19 | Bengaluru International Airport |  | IN | 638 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 596 |
| 22 | Congonhas Airport |  | BR | 579 |
| 23 | Charlotte/Douglas International Airport |  | US | 577 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 570 |
| 26 | Tenerife Norte Airport |  | ES | 557 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 535 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 530 |
| 30 | Barcelona International Airport |  | ES | 506 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 497 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 491 |
| 34 | Vitoria/Foronda Airport |  | ES | 479 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 473 |
| 36 | Don Mueang International Airport |  | TH | 462 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 462 |
| 38 | Amsterdam Airport Schiphol |  | NL | 461 |
| 39 | O. R. Tambo International Airport |  | ZA | 451 |
| 40 | Calgary International Airport |  | CA | 436 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 365 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 257 | 21m | 244 km | 1,082.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 182 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 111 | 27m | 215 km | 411.1 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 110 | 20m | 147 km | 278.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 98 | 1h 43m | 1,423 km | 2,405.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 95 | 23m | 55 km | 90.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 91 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ISR887 | ISR | Ben Gurion International Airport (LLBG) | Erzincan Airport (LTCD) | 2026-05-08 14:02 UTC | 2026-05-08 15:40 UTC | 1h 38m |
| COBALT1 | COB | Rye Field (MS63) | Rye Field (MS63) | 2026-05-08 15:23 UTC | 2026-05-08 15:37 UTC | 14m |
| OKSTK | OKS | Pribram Airport (LKPM) | Pribram Airport (LKPM) | 2026-05-08 15:06 UTC | 2026-05-08 15:36 UTC | 30m |
| N872SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-08 14:36 UTC | 2026-05-08 15:29 UTC | 52m |
| N789FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-08 13:57 UTC | 2026-05-08 15:27 UTC | 1h 30m |
| N570JA |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-05-08 15:01 UTC | 2026-05-08 15:27 UTC | 26m |
| N54TS |  | Republic Airport (KFRG) | Westmoreland Airport (49NY) | 2026-05-08 14:37 UTC | 2026-05-08 15:18 UTC | 40m |
| DAL2819 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 14:51 UTC | 2026-05-08 15:13 UTC | 21m |
| FGXBJ | FGX | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | 2026-05-08 15:11 UTC | 2026-05-08 15:11 UTC | 0m |
| N2776E |  | Augusta Regional At Bush Field (KAGS) | Aiken Regional Airport (KAIK) | 2026-05-08 14:42 UTC | 2026-05-08 15:09 UTC | 27m |
| IFJ43B | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-05-08 14:56 UTC | 2026-05-08 15:09 UTC | 12m |
|  |  | Chavenay Villepreux Airport (LFPX) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-05-08 15:02 UTC | 2026-05-08 15:08 UTC | 6m |
| N893HF |  | Melbourne Orlando International Airport (KMLB) | 21FA (21FA) | 2026-05-08 15:02 UTC | 2026-05-08 15:08 UTC | 5m |
| N13HN |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-05-08 14:52 UTC | 2026-05-08 15:08 UTC | 15m |
| N12997 |  | Wausau Downtown Airport (KAUW) | Merrill Municipal Airport (KRRL) | 2026-05-08 14:37 UTC | 2026-05-08 15:07 UTC | 29m |
| CHX50 | CHX | Hamburg Airport (EDDH) | Hamburg-Finkenwerder Airport (EDHI) | 2026-05-08 14:59 UTC | 2026-05-08 15:03 UTC | 4m |
| N361ML |  | Lake Havasu City Airport (KHII) | AZ77 (AZ77) | 2026-05-08 14:37 UTC | 2026-05-08 15:03 UTC | 26m |
| N930RA |  | Easterwood Field (KCLL) | Calico Rock Municipal Airport (K37T) | 2026-05-08 13:46 UTC | 2026-05-08 14:59 UTC | 1h 13m |
| N193AE |  | 4IS1 (4IS1) | Frasca Field (KC16) | 2026-05-08 14:44 UTC | 2026-05-08 14:57 UTC | 12m |
| N471AT |  | FA44 (FA44) | Palm Beach County Park Airport (KLNA) | 2026-05-08 14:42 UTC | 2026-05-08 14:57 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
