/**
 * Ashikur Rahman (favouritesir.me) Portfolio Engine
 * Deep Three.js 3D Parallax & Journey, Multi-Layer Tilt & Cursor Spotlight
 */

document.addEventListener('DOMContentLoaded', () => {
  initCursorSpotlight();
  initNavbar();
  initTypewriter();
  initUniversalCardTilt();
  initFloatingElementsParallax();
  initThreeJourney();
});

/* ==========================================================================
   1. CURSOR SPOTLIGHT
   ========================================================================== */
function initCursorSpotlight() {
  const glow = document.getElementById('cursor-glow');
  if (!glow) return;

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let currentX = mouseX;
  let currentY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  function renderGlow() {
    currentX += (mouseX - currentX) * 0.12;
    currentY += (mouseY - currentY) * 0.12;
    glow.style.left = `${currentX}px`;
    glow.style.top = `${currentY}px`;
    requestAnimationFrame(renderGlow);
  }
  renderGlow();
}

/* ==========================================================================
   2. NAVBAR & NAVIGATION
   ========================================================================== */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  const links = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    highlightCurrentSection();
  });

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });

    links.forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
      });
    });
  }

  function highlightCurrentSection() {
    const sections = document.querySelectorAll('section[id]');
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 140;
      const sectionId = current.getAttribute('id');
      const activeLink = document.querySelector(`.nav-link[href*="${sectionId}"]`);

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        links.forEach(l => l.classList.remove('active'));
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }
}

/* ==========================================================================
   3. TYPEWRITER EFFECT
   ========================================================================== */
function initTypewriter() {
  const typedTarget = document.getElementById('typed-text');
  if (!typedTarget) return;

  const phrases = [
    'Algorithm Researcher',
    'Conceived Cloud Sort (DOI: 10.5281/zenodo.23665548)',
    'In-Place Infix-to-Prefix (DOI: 10.5281/zenodo.23657544)',
    'Full-Stack & Systems Engineer',
    'Embedded IoT & Serverless Architect'
  ];

  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 65;

  function type() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
      typedTarget.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
      typingSpeed = 30;
    } else {
      typedTarget.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
      typingSpeed = 70;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
      isDeleting = true;
      typingSpeed = 1900;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typingSpeed = 350;
    }

    setTimeout(type, typingSpeed);
  }

  type();
}

/* ==========================================================================
   4. UNIVERSAL 3D CARD TILT & SPECULAR HIGHLIGHT
   ========================================================================== */
function initUniversalCardTilt() {
  const cards = document.querySelectorAll('.research-card, .project-card, .skill-category, #hero-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    });
  });
}

/* ==========================================================================
   5. DOM FLOATING ELEMENTS MOUSE PARALLAX
   ========================================================================== */
function initFloatingElementsParallax() {
  const heroVisual = document.querySelector('.hero-visual');
  const badges = document.querySelectorAll('.float-badge');
  const stats = document.querySelectorAll('.stat-card');

  window.addEventListener('mousemove', (e) => {
    const mouseNormX = (e.clientX / window.innerWidth) - 0.5;
    const mouseNormY = (e.clientY / window.innerHeight) - 0.5;

    badges.forEach((b, index) => {
      const depth = (index + 1) * 22;
      b.style.transform = `translate3d(${mouseNormX * depth}px, ${mouseNormY * depth}px, 50px)`;
    });

    stats.forEach((s, index) => {
      const depth = (index % 2 === 0 ? 1 : -1) * 8;
      s.style.transform = `translate3d(${mouseNormX * depth}px, ${mouseNormY * depth}px, 0)`;
    });
  });
}

/* ==========================================================================
   6. DEEP THREE.JS 3D JOURNEY & SCROLL-CAMERA PARALLAX
   ========================================================================== */
function initThreeJourney() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas || typeof THREE === 'undefined') return;

  // Scene & Camera
  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x080c16, 0.007);

  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.set(0, 0, 42);

  // Renderer
  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Lights
  const ambientLight = new THREE.AmbientLight(0x0f172a, 3.0);
  scene.add(ambientLight);

  const pointLight1 = new THREE.PointLight(0x00f0ff, 3.5, 120);
  pointLight1.position.set(25, 20, 30);
  scene.add(pointLight1);

  const pointLight2 = new THREE.PointLight(0x818cf8, 3.0, 120);
  pointLight2.position.set(-25, -40, 25);
  scene.add(pointLight2);

  const pointLight3 = new THREE.PointLight(0x10b981, 2.5, 100);
  pointLight3.position.set(0, -120, 20);
  scene.add(pointLight3);

  // ==========================================
  // 1. STARFIELD / PARTICLE CYBERSPACE TUNNEL
  // ==========================================
  const particleCount = 2200;
  const particleGeometry = new THREE.BufferGeometry();
  const particlePositions = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount * 3; i += 3) {
    particlePositions[i] = (Math.random() - 0.5) * 180;      // X
    particlePositions[i + 1] = (Math.random() * -300) + 30;  // Y spans down from +30 to -270
    particlePositions[i + 2] = (Math.random() - 0.5) * 120;  // Z
  }

  particleGeometry.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));

  // Particle Texture
  const pCanvas = document.createElement('canvas');
  pCanvas.width = 16;
  pCanvas.height = 16;
  const pCtx = pCanvas.getContext('2d');
  const gradient = pCtx.createRadialGradient(8, 8, 0, 8, 8, 8);
  gradient.addColorStop(0, 'rgba(0, 240, 255, 1)');
  gradient.addColorStop(0.35, 'rgba(129, 140, 248, 0.7)');
  gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
  pCtx.fillStyle = gradient;
  pCtx.fillRect(0, 0, 16, 16);

  const particleTexture = new THREE.CanvasTexture(pCanvas);

  const particleMaterial = new THREE.PointsMaterial({
    size: 2.2,
    map: particleTexture,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    color: 0x38bdf8
  });

  const particleSystem = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particleSystem);

  // ==========================================
  // 2. HERO MONUMENT: Rotating 3D Geodesic Core (Y = 0)
  // ==========================================
  const heroGroup = new THREE.Group();
  heroGroup.position.set(16, 0, -8);
  scene.add(heroGroup);

  const icoGeo = new THREE.IcosahedronGeometry(13, 1);
  const icoMat = new THREE.MeshStandardMaterial({
    color: 0x00d2ff,
    wireframe: true,
    emissive: 0x00599c,
    emissiveIntensity: 0.4,
    metalness: 0.8,
    roughness: 0.2
  });
  const icosahedron = new THREE.Mesh(icoGeo, icoMat);
  heroGroup.add(icosahedron);

  const ringGeo1 = new THREE.TorusGeometry(19, 0.3, 16, 100);
  const ringMat1 = new THREE.MeshBasicMaterial({ color: 0x818cf8, wireframe: true, transparent: true, opacity: 0.45 });
  const ring1 = new THREE.Mesh(ringGeo1, ringMat1);
  ring1.rotation.x = Math.PI / 3;
  heroGroup.add(ring1);

  const ringGeo2 = new THREE.TorusGeometry(22, 0.2, 16, 100);
  const ringMat2 = new THREE.MeshBasicMaterial({ color: 0x00f0ff, wireframe: true, transparent: true, opacity: 0.3 });
  const ring2 = new THREE.Mesh(ringGeo2, ringMat2);
  ring2.rotation.y = Math.PI / 4;
  heroGroup.add(ring2);

  // ==========================================
  // 3. RESEARCH MONUMENT: Cloud Sort Dual-Plane Hierarchy (Y = -60)
  // ==========================================
  const researchGroup = new THREE.Group();
  researchGroup.position.set(-18, -60, -10);
  scene.add(researchGroup);

  // Cloud Buffer Upper Plane
  const cloudGridGeo = new THREE.PlaneGeometry(28, 12, 10, 5);
  const cloudGridMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.55 });
  const cloudPlane = new THREE.Mesh(cloudGridGeo, cloudGridMat);
  cloudPlane.rotation.x = -Math.PI / 2.6;
  cloudPlane.position.y = 7;
  researchGroup.add(cloudPlane);

  // Ground Array Lower Plane
  const groundGridGeo = new THREE.PlaneGeometry(36, 16, 14, 6);
  const groundGridMat = new THREE.MeshBasicMaterial({ color: 0x10b981, wireframe: true, transparent: true, opacity: 0.45 });
  const groundPlane = new THREE.Mesh(groundGridGeo, groundGridMat);
  groundPlane.rotation.x = -Math.PI / 2.6;
  groundPlane.position.y = -7;
  researchGroup.add(groundPlane);

  // Data Ascension Energy Pillars (Connecting Cloud & Ground)
  const lineMat = new THREE.LineBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.65 });
  for (let i = -10; i <= 10; i += 4) {
    const lineGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(i, -7, 0),
      new THREE.Vector3(i * 0.7, 7, 0)
    ]);
    const line = new THREE.Line(lineGeo, lineMat);
    researchGroup.add(line);
  }

  // ==========================================
  // 4. PROJECTS MONUMENT: Microservice Polyhedra Array (Y = -120)
  // ==========================================
  const projectsGroup = new THREE.Group();
  projectsGroup.position.set(18, -120, -10);
  scene.add(projectsGroup);

  const octGeo = new THREE.OctahedronGeometry(8, 0);
  const octMat = new THREE.MeshStandardMaterial({
    color: 0xc084fc,
    wireframe: true,
    emissive: 0x6b21a8,
    emissiveIntensity: 0.5
  });
  const octahedron = new THREE.Mesh(octGeo, octMat);
  projectsGroup.add(octahedron);

  const boxGeo = new THREE.BoxGeometry(14, 14, 14);
  const boxMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.35 });
  const wireBox = new THREE.Mesh(boxGeo, boxMat);
  projectsGroup.add(wireBox);

  // ==========================================
  // 5. SKILLS MONUMENT: Pulsing Torus Knot (Y = -180)
  // ==========================================
  const skillsGroup = new THREE.Group();
  skillsGroup.position.set(-15, -180, -10);
  scene.add(skillsGroup);

  const knotGeo = new THREE.TorusKnotGeometry(9, 2.2, 100, 16);
  const knotMat = new THREE.MeshStandardMaterial({
    color: 0x10b981,
    wireframe: true,
    emissive: 0x047857,
    emissiveIntensity: 0.4
  });
  const torusKnot = new THREE.Mesh(knotGeo, knotMat);
  skillsGroup.add(torusKnot);

  // ==========================================
  // 6. CONTACT MONUMENT: Crystalline Dodecahedron (Y = -240)
  // ==========================================
  const contactGroup = new THREE.Group();
  contactGroup.position.set(0, -240, -12);
  scene.add(contactGroup);

  const dodecaGeo = new THREE.DodecahedronGeometry(10, 0);
  const dodecaMat = new THREE.MeshStandardMaterial({
    color: 0x38bdf8,
    wireframe: true,
    emissive: 0x0284c7,
    emissiveIntensity: 0.5
  });
  const dodecahedron = new THREE.Mesh(dodecaGeo, dodecaMat);
  contactGroup.add(dodecahedron);

  // --- Dynamic Parallax State ---
  let mouseX = 0;
  let mouseY = 0;
  let targetMouseX = 0;
  let targetMouseY = 0;
  let scrollProgress = 0;
  let targetCameraY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
  });

  window.addEventListener('scroll', () => {
    const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
    scrollProgress = totalScroll > 0 ? window.scrollY / totalScroll : 0;
  });

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  });

  // --- Animation Loop ---
  const clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);

    const elapsedTime = clock.getElapsedTime();

    // Responsive Mouse Lerp
    targetMouseX += (mouseX - targetMouseX) * 0.08;
    targetMouseY += (mouseY - targetMouseY) * 0.08;

    // Camera travels smoothly down the Y axis through all sections
    targetCameraY = -scrollProgress * 240;
    camera.position.y += (targetCameraY - camera.position.y) * 0.08;

    // Strong Mouse Parallax Sway on Camera
    camera.position.x += (targetMouseX * 18 - camera.position.x) * 0.06;
    camera.position.z = 42 + Math.sin(scrollProgress * Math.PI * 2) * 6;

    camera.rotation.y = -targetMouseX * 0.12;
    camera.rotation.x = targetMouseY * 0.08;

    // Rotate Monuments
    heroGroup.rotation.y = elapsedTime * 0.2;
    icosahedron.rotation.x = elapsedTime * 0.25;
    ring1.rotation.z = elapsedTime * 0.15;
    ring2.rotation.y = -elapsedTime * 0.2;

    researchGroup.rotation.y = Math.sin(elapsedTime * 0.5) * 0.3;
    cloudPlane.rotation.z = elapsedTime * 0.1;
    groundPlane.rotation.z = -elapsedTime * 0.08;

    projectsGroup.rotation.x = elapsedTime * 0.18;
    projectsGroup.rotation.y = elapsedTime * 0.25;
    octahedron.rotation.z = -elapsedTime * 0.3;

    skillsGroup.rotation.y = elapsedTime * 0.22;
    torusKnot.rotation.x = elapsedTime * 0.15;

    contactGroup.rotation.y = elapsedTime * 0.3;
    contactGroup.rotation.x = elapsedTime * 0.2;

    // Rotate Particle Universe
    particleSystem.rotation.y = elapsedTime * 0.02 + targetMouseX * 0.05;

    renderer.render(scene, camera);
  }

  animate();
}
