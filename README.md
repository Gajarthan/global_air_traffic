# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_19:19:06_UTC-green)

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

**Latest saved flight:** 2026-04-21 19:19:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 19:19:06 UTC

- **47,100** saved flights
- **19,262** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,100** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **565,777.2 tonnes** estimated CO2 emissions
- **32,798,681 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2004 |
| 2 | SkyWest Airlines | 1818 |
| 3 | IndiGo | 1106 |
| 4 | EJA | 806 |
| 5 | American Airlines | 777 |
| 6 | Southwest Airlines | 673 |
| 7 | ENY | 611 |
| 8 | Lufthansa | 508 |
| 9 | Vueling | 475 |
| 10 | AXM | 470 |
| 11 | LATAM Airlines | 465 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 402 |
| 14 | Delta Air Lines | 391 |
| 15 | WIF | 379 |
| 16 | QLK | 376 |
| 17 | LXJ | 365 |
| 18 | Swiss International | 362 |
| 19 | AEE | 321 |
| 20 | Alaska Airlines | 320 |
| 21 | EJU | 314 |
| 22 | easyJet | 300 |
| 23 | VIV | 300 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 250 |
| 27 | JetBlue | 250 |
| 28 | AXB | 248 |
| 29 | United Airlines | 248 |
| 30 | GLO | 238 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37391 |
| 2 | 🇮🇳 IN | 3440 |
| 3 | 🇪🇸 ES | 3431 |
| 4 | 🇦🇺 AU | 3235 |
| 5 | 🇧🇷 BR | 2763 |
| 6 | 🇯🇵 JP | 2571 |
| 7 | 🇮🇹 IT | 2562 |
| 8 | 🇩🇪 DE | 2446 |
| 9 | 🇨🇦 CA | 2304 |
| 10 | 🇨🇴 CO | 2190 |
| 11 | 🇬🇧 GB | 1926 |
| 12 | 🇫🇷 FR | 1800 |
| 13 | 🇲🇽 MX | 1461 |
| 14 | 🇬🇷 GR | 1442 |
| 15 | 🇨🇭 CH | 1297 |
| 16 | 🇳🇴 NO | 1210 |
| 17 | 🇲🇾 MY | 1147 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 913 |
| 20 | 🇹🇭 TH | 846 |
| 21 | 🇵🇭 PH | 833 |
| 22 | 🇹🇷 TR | 827 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 743 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 584 |
| 27 | 🇲🇪 ME | 501 |
| 28 | 🇳🇱 NL | 482 |
| 29 | 🇲🇴 MO | 441 |
| 30 | 🇧🇸 BS | 423 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1106 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 781 |
| 4 | El Dorado International Airport |  | CO | 762 |
| 5 | Indira Gandhi International Airport |  | IN | 736 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 713 |
| 7 | Guaymaral Airport |  | CO | 610 |
| 8 | Harry Reid International Airport |  | US | 606 |
| 9 | Zurich Airport |  | CH | 561 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 480 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 466 |
| 13 | Chicago O'Hare International Airport |  | US | 461 |
| 14 | Kuala Lumpur International Airport |  | MY | 460 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 450 |
| 16 | Macau International Airport |  | MO | 441 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 418 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 404 |
| 21 | Malpensa International Airport |  | IT | 400 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 394 |
| 24 | Ninoy Aquino International Airport |  | PH | 385 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 357 |
| 26 | Salt Lake City International Airport |  | US | 354 |
| 27 | Daniel K Inouye International Airport |  | US | 351 |
| 28 | Charles de Gaulle International Airport |  | FR | 350 |
| 29 | Capua Airport |  | IT | 349 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 344 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 325 |
| 32 | Reno/Tahoe International Airport |  | US | 323 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 320 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | O. R. Tambo International Airport |  | ZA | 313 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 37 | Barcelona International Airport |  | ES | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 282 |
| 40 | Viracopos International Airport |  | BR | 280 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 245 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 179 | 14m | 114 km | 351.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 138 | 21m | 244 km | 581.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 76 | 20m | 147 km | 192.3 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 75 | 52m | 556 km | 718.9 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 0m | 695 km | 779.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 64 | 16m | 162 km | 179.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N508FG |  | Hackenburg-Penny Hill Airport (6PA3) | Lancaster Airport (KLNS) | 2026-04-21 18:30 UTC | 2026-04-21 19:19 UTC | 48m |
| N738HD |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-04-21 18:58 UTC | 2026-04-21 19:18 UTC | 19m |
| N98561 |  | Butler County Regional/Hogan Field (KHAO) | Richmond Municipal Airport (KRID) | 2026-04-21 19:00 UTC | 2026-04-21 19:15 UTC | 14m |
| N58BK |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-04-21 18:54 UTC | 2026-04-21 19:14 UTC | 19m |
| RNGR713 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-04-21 18:42 UTC | 2026-04-21 19:08 UTC | 26m |
| BOXER96 | BOX | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-04-21 18:49 UTC | 2026-04-21 19:01 UTC | 12m |
| CFORE | CFO | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Cooking Lake Airport (CEZ3) | 2026-04-21 18:33 UTC | 2026-04-21 18:56 UTC | 22m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-21 18:07 UTC | 2026-04-21 18:56 UTC | 48m |
| LXJ618 | LXJ | Teterboro Airport (KTEB) | Orlando Executive Airport (KORL) | 2026-04-21 16:47 UTC | 2026-04-21 18:56 UTC | 2h 9m |
| N682EE |  | Melbourne Orlando International Airport (KMLB) | Melbourne Orlando International Airport (KMLB) | 2026-04-21 18:22 UTC | 2026-04-21 18:53 UTC | 30m |
| IWY742 | IWY | Sir Grantley Adams International Airport (TBPB) | Hewanorra International Airport (TLPL) | 2026-04-21 18:30 UTC | 2026-04-21 18:51 UTC | 20m |
| BL87L |  | Gulf Shores International/Jack Edwards Field (KJKA) | Jeremiah Denton Airport (K4R9) | 2026-04-21 18:34 UTC | 2026-04-21 18:50 UTC | 16m |
| NSZ3646 | NSZ | Copenhagen Kastrup Airport (EKCH) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-21 16:57 UTC | 2026-04-21 18:49 UTC | 1h 52m |
| CFSUG | CFS | Calgary International Airport (CYYC) | Irma Airport (CFU8) | 2026-04-21 18:12 UTC | 2026-04-21 18:47 UTC | 35m |
| VM559 |  | Nellis Afb Airport (KLSV) | Walter's Camp Airport (CN98) | 2026-04-21 17:47 UTC | 2026-04-21 18:47 UTC | 59m |
| AR3 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-04-21 18:38 UTC | 2026-04-21 18:40 UTC | 1m |
| N900XL |  | Manassas Regional/Harry P Davis Field (KHEF) | 32VA (32VA) | 2026-04-21 18:00 UTC | 2026-04-21 18:40 UTC | 40m |
| EJA279 | EJA | Van Nuys Airport (KVNY) | Scottsdale Airport (KSDL) | 2026-04-21 17:43 UTC | 2026-04-21 18:39 UTC | 55m |
| PSVLS | PSV | Congonhas Airport (SBSP) | Fazenda Planalto Airport (SSMX) | 2026-04-21 17:52 UTC | 2026-04-21 18:37 UTC | 45m |
| WIF2WK | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-04-21 18:04 UTC | 2026-04-21 18:36 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
