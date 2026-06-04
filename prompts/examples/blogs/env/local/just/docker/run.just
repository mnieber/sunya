import './build.just'
import './lib/_up.just'
import './lib/_down.just'
import './lib/_run_image.just'

up use_dockerfile_local: \
    (_touch_compose_override) \
    (compile-env-files) \
    (_up use_dockerfile_local "true" "true")

down: (compile-env-files) (_down "true" "true")

restart use_dockerfile_local=default_use_dockerfile_local use_no_cache="false": \
    (down) \
    (build use_dockerfile_local use_no_cache) \
    (up use_dockerfile_local) \

shell service_name: (compile-env-files) (_run_image service_name "true" "true" "true" "fish")
